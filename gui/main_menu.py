from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import functools

from gui import history_screen
from gui.history_screen import HistoryScreen
from gui.rsa_screen import RSAScreen
fp = functools.partial
from .playfair_screen import PlayFairScreen

# ------------------ VerticalScrolledFrame ------------------
class VerticalScrolledFrame(ttk.Frame):
    def __init__(self, parent, sidebar=None, *args, **kw):
        self.sidebar = sidebar

        def _configure_interior(event):
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                canvas.config(width=interior.winfo_reqwidth())

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        def _bind_to_mousewheel(event):
            canvas.bind_all("<MouseWheel>", _on_mousewheel)
        def _unbind_from_mousewheel(event):
            canvas.unbind_all("<MouseWheel>")

        ttk.Frame.__init__(self, parent, *args, **kw)

        vscrollbar = ttk.Scrollbar(self, orient=VERTICAL)
        if self.sidebar and getattr(self.sidebar, "show_scrollbar", False):
            vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self, bd=0, highlightthickness=0, yscrollcommand=vscrollbar.set)
        self.canvas = canvas
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview)

        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior, anchor=NW)

        interior.bind('<Configure>', _configure_interior)
        canvas.bind('<Configure>', _configure_canvas)
        canvas.bind('<Enter>', _bind_to_mousewheel)
        canvas.bind('<Leave>', _unbind_from_mousewheel)

# ------------------ ImageProcessor / Sprite ------------------
def Sprite(picture, res1, res2):
    im = Image.open(picture).convert("RGBA").resize((res1, res2), Image.BOX)
    pic = ImageTk.PhotoImage(im)
    return pic

# ------------------ Controls: Spacer & Button ------------------
class SideBarSpacer(Canvas):
    def __init__(self, parent, text, *args, **kwargs):
        self.frame_color = "#232323"
        self.hover_border_color = "grey"
        Canvas.__init__(self, parent, width=199, height=35, bg=self.frame_color, highlightthickness=1, highlightbackground=self.frame_color, *args, **kwargs)
        self.pack()
        self.text = Label(self, text=text, bg=self.frame_color, font="Segoe 10 bold", fg="lightgrey")
        self.text.place(x=3, y=12)
    def hover(self, event=None):
        self.config(highlightbackground=self.hover_border_color)
    def unhover(self, event=None):
        self.config(highlightbackground=self.frame_color)
    def click(self, event=None):
        print()

class SideBarButton(Canvas):
    def __init__(self, parent, text, command, icon=None, tab=False, *args, **kwargs):
        self.frame_color = "#232323"
        self.hover_color = "#4D4c4c"
        self.hover_border_color = "grey"
        self.is_tab = tab
        self.selected = False
        self.command = command

        Canvas.__init__(self, parent, width=198, height=35, bg=self.frame_color, highlightthickness=1, highlightbackground=self.frame_color, *args, **kwargs)
        self.pack()

        if icon:
            self.icon = Sprite(icon, 20, 20)
            self.create_image(20, 20, image=self.icon)

        self.text = Label(self, text=text, font="Segoe 10", bg=self.frame_color, fg="lightgrey")
        self.text.place(x=40, y=10)

        self.bind('<Enter>', self.hover)
        self.bind('<Button-1>', self.click)
        if not self.is_tab:
            self.bind('<ButtonRelease-1>', self.unclick)

        self.text.bind('<Enter>', self.hover)
        self.text.bind('<Button-1>', self.click)
        if not self.is_tab:
            self.text.bind('<ButtonRelease-1>', self.unclick)

    def hover(self, event=None):
        if not self.selected:
            self.bind('<Leave>', self.unhover)
            self.config(highlightbackground=self.hover_border_color, bg=self.hover_color)
            self.text.config(bg=self.hover_color)
    def unhover(self, event=None):
        self.config(highlightbackground=self.frame_color, bg=self.frame_color)
        self.text.config(bg=self.frame_color)
    def click(self, event=None):
        if self.is_tab:
            self.bind('<Leave>', str)
        self.selected = True
        self.config(bg=self.hover_border_color)
        self.text.config(bg=self.hover_border_color)
        self.command()
    def unclick(self, event=None):
        self.selected = False
        self.config(bg=self.hover_color)
        self.text.config(bg=self.hover_color)

# ------------------ Sidebar ------------------
class Sidebar(VerticalScrolledFrame):
    def __init__(self, parent, width=200, show_scrollbar=False):
        self.show_scrollbar = show_scrollbar
        super().__init__(parent, self)
        self.config(width=width)
        self.interior.config(bg="#232323")
        self.canvas.config(bg="#232323")
        self.pack_propagate(0)
        self.pack(expand=False, side=LEFT, fill=Y)

    def add_spacer(self, text):
        SideBarSpacer(self.interior, text)

    def add_button(self, text, command, icon=None):
        SideBarButton(self.interior, text, command, icon)

# ------------------ Main Menu Screen ------------------
class MainMenu(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.pack(fill=BOTH, expand=True)

        # Sidebar
        sidebar = Sidebar(self, show_scrollbar=False)
        sidebar.add_spacer("Menu")
        sidebar.add_button("Home", self.show_home)
        sidebar.add_button("PlayFair", self.show_playfair)
        sidebar.add_button("RSA", self.show_rsa)
        sidebar.add_button("History", self.show_history)

        self.content = Frame(self, bg="#d9d9d9")
        self.content.pack(side=LEFT, fill=BOTH, expand=True)

        self.show_home()

    # ------------------ Clear Content ------------------
    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    # ------------------ Trang Home ------------------
    def show_home(self):
        self.clear_content()

        top_panel = Frame(self.content, bg="white", bd=1, relief=GROOVE)
        top_panel.pack(fill=X, padx=20, pady=(20, 10))

        title = Label(
            top_panel,
            text="MÔN HỌC:\nAN TOÀN MẠNG MÁY TÍNH",
            bg="white",
            fg="#111",
            font=("Times New Roman", 24, "bold"),
            justify=CENTER
        )
        title.pack(pady=(18, 6))

        class_label = Label(
            top_panel,
            text="Mã Lớp:  NT101.Q13 - Nhóm 13",
            bg="white",
            fg="#111",
            font=("Times New Roman", 14, "italic")
        )
        class_label.pack(pady=(0, 12))

        topic_frame = Frame(top_panel, bg="white")
        topic_frame.pack(fill=X, padx=18, pady=(0, 18))
        topic_label_title = Label(topic_frame, text="Đề tài:", bg="white", fg="#111", font=("Segoe UI", 12, "bold"))
        topic_label_title.grid(row=0, column=0, sticky=W)
        topic_label = Label(topic_frame, text="Viết ứng dụng mô phỏng các giải thuật mã hóa Playfair và RSA", bg="white", fg="#111", font=("Segoe UI", 12, "italic"))
        topic_label.grid(row=0, column=1, sticky=W, padx=(8,0))

        lower_panel = Frame(self.content, bg="#d9d9d9")
        lower_panel.pack(fill=BOTH, expand=True, padx=20, pady=(6,20))

        info_card = Frame(lower_panel, bg="white", bd=1, relief=GROOVE)
        info_card.pack(side=LEFT, fill=BOTH, expand=True, padx=(0,12), pady=6)
        info_inner = Frame(info_card, bg="white")
        info_inner.pack(padx=20, pady=20, fill=BOTH, expand=True)

        gv_label = Label(info_inner, text="GVHD: ThS. Tô Nguyễn Nhật Quang", bg="white", fg="#111", font=("Segoe UI", 18, "bold"))
        gv_label.grid(row=0, column=0, sticky=W)

        sv_label = Label(info_inner, text="Sinh viên thực hiện:", bg="white", fg="#111", font=("Segoe UI", 16, "bold"))
        sv_label.grid(row=1, column=0, sticky=W, pady=(12,0))

        students_frame = Frame(info_inner, bg="white")
        students_frame.grid(row=2, column=0, columnspan=2, sticky=W, pady=(8,0))
        students = [
            "23521549 - Huỳnh Ngọc Thuận",
            "23521823 - Nguyễn Quốc Vương",
            "23521228 - Bùi Lê Huy Phước"
        ]
        for i, s in enumerate(students):
            Label(students_frame, text=s, bg="white", fg="#111", font=("Segoe UI", 14)).pack(anchor=W)

        features_panel = Frame(lower_panel, bg="#d9d9d9", width=260)
        features_panel.pack(side=RIGHT, fill=Y, pady=6)
        features_panel.pack_propagate(False)

        features_box = Frame(features_panel, bg="white", bd=1, relief=GROOVE)
        features_box.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.9, relheight=0.9)

        def create_small_feature(parent, title, desc, command):
            card = Frame(parent, bg="white", width=200, height=60, highlightthickness=1, highlightbackground="#cfcfcf")
            card.pack_propagate(False)
            card.pack(pady=30, padx=30)

            btn = Button(card, text=title, command=command, font=("Segoe UI", 12, "bold"))
            btn.pack(fill=BOTH, expand=True, padx=6, pady=6)
            return card

        create_small_feature(features_box, "PlayFair", "", self.show_playfair)
        create_small_feature(features_box, "RSA", "", self.show_rsa)
        create_small_feature(features_box, "History", "", self.show_history)


    # ------------------ Trang PlayFair ------------------
    def show_playfair(self):
        self.clear_content()
        PlayFairScreen(self.content).pack(fill=BOTH, expand=True)

    # ------------------ Trang RSA ------------------
    def show_rsa(self):
        self.clear_content()
        RSAScreen(self.content, self).pack(fill=BOTH, expand=True)

    # ------------------ Trang History ------------------
    def show_history(self):
        self.clear_content()
        history_screen = HistoryScreen(self.content)
        history_screen.pack(fill=BOTH, expand=True)