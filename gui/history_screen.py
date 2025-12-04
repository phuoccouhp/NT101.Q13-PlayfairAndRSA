from tkinter import *
from tkinter import ttk
import json
import os

class HistoryScreen(Frame):
    def __init__(self, master):
        super().__init__(master, bg="#d9d9d9")

        # ===== Tiêu đề =====
        Label(
            self,
            text="Lịch sử mã hóa và giải mã",
            bg="#d9d9d9",
            fg="black",
            font=("Segoe UI", 18, "bold")
        ).pack(pady=20)

        # ===== Khung chứa bảng =====
        table_frame = Frame(self, bg="#d9d9d9")
        table_frame.pack(fill=BOTH, expand=True, padx=25, pady=10)

        # ===== Scrollbar =====
        y_scroll = ttk.Scrollbar(table_frame, orient=VERTICAL)
        y_scroll.pack(side=RIGHT, fill=Y)

        x_scroll = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        x_scroll.pack(side=BOTTOM, fill=X)

        # ===== Bảng hiển thị dữ liệu =====
        self.tree = ttk.Treeview(
            table_frame,
            columns=("name", "type", "text", "key", "result", "timestamp"),
            show="headings",
            yscrollcommand=y_scroll.set,
            xscrollcommand=x_scroll.set,
            height=15
        )
        self.tree.pack(fill=BOTH, expand=True)
        y_scroll.config(command=self.tree.yview)
        x_scroll.config(command=self.tree.xview)

        columns = {
            "name": "Tên bản ghi",
            "type": "Thuật toán",
            "text": "Văn bản",
            "key": "Khóa",
            "result": "Kết quả",
            "timestamp": "Thời gian"
        }

        for col, text in columns.items():
            self.tree.heading(col, text=text)
            self.tree.column(col, anchor="center", width=150, minwidth=120)

        # ===== Nút xóa bản ghi / xóa tất cả =====
        button_frame = Frame(self, bg="#d9d9d9")
        button_frame.pack(pady=10)

        btn_style = {
            "width": 18,
            "height": 1,
            "bg": "#d32f2f",        # màu đỏ nổi bật
            "fg": "white",           # chữ màu trắng
            "font": ("Segoe UI", 10, "bold"),
            "activebackground": "#d32f2f",  # khi nhấn nút
            "activeforeground": "white",
            "bd": 0,
            "relief": "raised"
        }

        delete_btn = Button(button_frame, text="Xóa bản ghi", command=self.delete_selected, **btn_style)
        delete_btn.pack(side=LEFT, padx=5)

        delete_all_btn = Button(button_frame, text="Xóa tất cả", command=self.delete_all, **btn_style)
        delete_all_btn.pack(side=LEFT, padx=5)

        # ===== Load lịch sử khi mở màn hình =====
        self.load_history()

    # ===== Hàm load lịch sử =====
    def load_history(self):
        self.tree.delete(*self.tree.get_children())
        history_file = os.path.join("data", "history.json")
        if not os.path.exists(history_file):
            return
        try:
            with open(history_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return
        if not isinstance(data, list):
            return
        for record in reversed(data):
            self.tree.insert(
                "",
                "end",
                values=(
                    record.get("name", ""),
                    record.get("type", ""),
                    record.get("text", ""),
                    record.get("key", ""),
                    record.get("result", ""),
                    record.get("timestamp", "")
                )
            )

    # ===== Hiển thị popup thông báo giữa frame =====
    def show_centered_message(self, title, message):
        popup = Toplevel(self)
        popup.transient(self)
        popup.grab_set()
        popup.configure(bg="#d9d9d9")
        popup.geometry("+%d+%d" % (
            self.winfo_rootx() + self.winfo_width()//2 - 150,
            self.winfo_rooty() + self.winfo_height()//2 - 50
        ))
        popup.resizable(False, False)
        Label(popup, text=message, font=("Segoe UI", 11), bg="#d9d9d9", fg="black").pack(padx=20, pady=15)
        Button(popup, text="OK", width=10, command=popup.destroy, bg="#3498db", fg="white", font=("Segoe UI", 10, "bold")).pack(pady=(0,15))

    # ===== Xóa bản ghi đã chọn =====
    def delete_selected(self):
        selected = self.tree.selection()
        if not selected:
            self.show_centered_message("Thông báo", "Vui lòng chọn bản ghi để xóa!")
            return

        history_file = os.path.join("data", "history.json")
        if os.path.exists(history_file):
            with open(history_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            # Lọc bỏ các bản ghi được chọn
            for sel in selected:
                values = self.tree.item(sel, "values")
                data = [rec for rec in data if not (
                    rec.get("name","") == values[0] and
                    rec.get("timestamp","") == values[5]
                )]
            with open(history_file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

        # Xóa trên Treeview
        for sel in selected:
            self.tree.delete(sel)

    # ===== Xóa tất cả =====
    def delete_all(self):
        confirm = Toplevel(self)
        confirm.transient(self)
        confirm.grab_set()
        confirm.configure(bg="#d9d9d9")
        confirm.geometry("+%d+%d" % (
            self.winfo_rootx() + self.winfo_width()//2 - 160,
            self.winfo_rooty() + self.winfo_height()//2 - 60
        ))
        confirm.resizable(False, False)

        Label(confirm, text="Bạn có chắc muốn xóa tất cả bản ghi không?", font=("Segoe UI", 11), bg="#d9d9d9", fg="black").pack(padx=20, pady=15)

        btn_frame = Frame(confirm, bg="#d9d9d9")
        btn_frame.pack(pady=(0,15))

        Button(btn_frame, text="Có", width=10, command=lambda:[self._delete_all(confirm)], bg="#d32f2f", fg="white", font=("Segoe UI", 10, "bold")).pack(side=LEFT, padx=5)
        Button(btn_frame, text="Không", width=10, command=confirm.destroy, bg="#3498db", fg="white", font=("Segoe UI", 10, "bold")).pack(side=LEFT, padx=5)

    # Thực sự xóa tất cả và đóng popup
    def _delete_all(self, popup):
        history_file = os.path.join("data", "history.json")
        if os.path.exists(history_file):
            with open(history_file, "w", encoding="utf-8") as f:
                json.dump([], f)
        self.tree.delete(*self.tree.get_children())
        popup.destroy()
