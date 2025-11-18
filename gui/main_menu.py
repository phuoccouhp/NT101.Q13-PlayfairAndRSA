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

        # Main content placeholder
        self.content = Frame(self, bg="#d9d9d9")
        self.content.pack(side=LEFT, fill=BOTH, expand=True)

        # Hiển thị màn hình mặc định
        self.show_home()

    # ------------------ Clear Content ------------------
    def clear_content(self):
        """Xóa toàn bộ widget trong vùng nội dung chính."""
        for widget in self.content.winfo_children():
            widget.destroy()

    # ------------------ Trang Home ------------------
    def show_home(self):
        self.clear_content()

        # ===== Title =====
        title = Label(
            self.content,
            text="Cryptography Toolkit",
            bg="#d9d9d9",
            fg="#111",
            font=("Segoe UI", 26, "bold")
        )
        title.pack(pady=(25, 8))

        subtitle = Label(
            self.content,
            text=("Một công cụ mã hóa và giải mã các thuật toán mã hóa cổ điển & hiện đại. \n" 
            "Cryptography Toolkit – Mã hóa thông minh, giải mã tức thì, lưu giữ lịch sử chi tiết và bảo vệ mọi dữ liệu quan trọng của bạn. \n"
            "Tất cả trong một ứng dụng trực quan giúp bạn kiểm soát thông tin mọi lúc, mọi nơi"),
            bg="#d9d9d9",
            fg="#444",
            font=("Segoe UI", 12)
        )
        subtitle.pack()

        # ===== Feature Wrapper =====
        wrapper = Frame(self.content, bg="#d9d9d9")
        wrapper.pack(pady=40)

        # ===== Function to create modern card =====
        def create_modern_card(parent, title, desc, command):
            card = Frame(
                parent,
                bg="white",
                width=230,
                height=160,
                highlightthickness=1,
                highlightbackground="#cfcfcf"
            )
            card.pack_propagate(False)

            # Hover effect
            def on_enter(e):
                card.config(highlightbackground="#7a7a7a", bg="#fafafa")

            def on_leave(e):
                card.config(highlightbackground="#cfcfcf", bg="white")

            card.bind("<Enter>", on_enter)
            card.bind("<Leave>", on_leave)

            # Title
            Label(
                card,
                text=title,
                font=("Segoe UI", 13, "bold"),
                fg="#1a1a1a",
                bg="white"
            ).pack(pady=(15, 5))

            # Description
            Label(
                card,
                text=desc,
                font=("Segoe UI", 10),
                fg="#555",
                wraplength=180,
                justify="center",
                bg="white"
            ).pack(pady=(0, 10))

            # ===== Plus button =====
            plus_btn = Label(
                card,
                text="+",
                font=("Segoe UI", 26, "bold"),
                fg="#333",
                bg="white",
                cursor="hand2"
            )
            plus_btn.pack()

            plus_btn.bind("<Enter>", lambda e: plus_btn.config(fg="#000"))
            plus_btn.bind("<Leave>", lambda e: plus_btn.config(fg="#333"))
            plus_btn.bind("<Button-1>", lambda e: command())

            return card

        # ===== Cards Layout =====
        row = Frame(wrapper, bg="#d9d9d9")
        row.pack()

        card1 = create_modern_card(
            row,
            "PlayFair Cipher",
            "Mã hóa & giải mã bằng thuật toán PlayFair cổ điển.",
            self.show_playfair
        )
        card2 = create_modern_card(
            row,
            "RSA Encryption",
            "Tạo khóa, mã hóa và giải mã bằng RSA hiện đại.",
            self.show_rsa
        )
        card3 = create_modern_card(
            row,
            "History",
            "Xem lại tất cả thao tác mã hóa / giải mã đã thực hiện.",
            self.show_history
        )

        card1.grid(row=0, column=0, padx=25)
        card2.grid(row=0, column=1, padx=25)
        card3.grid(row=0, column=2, padx=25)


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
