from tkinter import *
from playfair.cipher import encrypt_playfair, decrypt_playfair
import json
import os
from datetime import datetime

class PlayFairScreen(Frame):
    def __init__(self, master):
        super().__init__(master, bg="#d9d9d9")

        # Tiêu đề
        Label(self, text="Mã hóa và giải mã PlayFair", bg="#d9d9d9", fg="black",
              font=("Segoe UI", 18, "bold")).pack(pady=20)

        # Frame chứa nội dung chính
        content = Frame(self, bg="#d9d9d9")
        content.pack(pady=10)

        # Từ khóa
        Label(content, text="Từ khóa:", bg="#d9d9d9", font=("Segoe UI", 12)).grid(row=0, column=0, sticky=E, padx=10, pady=8)
        self.key_entry = Entry(content, width=45, font=("Segoe UI", 12))
        self.key_entry.grid(row=0, column=1, pady=8)

        # Văn bản đầu vào
        Label(content, text="Văn bản:", bg="#d9d9d9", font=("Segoe UI", 12)).grid(row=1, column=0, sticky=E, padx=10, pady=8)
        self.input_text = Entry(content, width=45, font=("Segoe UI", 12))
        self.input_text.grid(row=1, column=1, pady=8)

        # Kết quả (Entry readonly để có thể copy)
        Label(content, text="Kết quả:", bg="#d9d9d9", font=("Segoe UI", 12)).grid(row=2, column=0, sticky=E, padx=10, pady=8)
        self.result_entry = Entry(content, width=45, font=("Segoe UI", 12), justify="center",
                                  state="readonly", fg="blue", readonlybackground="white")
        self.result_entry.grid(row=2, column=1, pady=8)

        # Frame chứa nút
        button_frame = Frame(self, bg="#d9d9d9")
        button_frame.pack(pady=15)

        Button(button_frame, text="Mã hóa", command=self.encrypt,
               font=("Segoe UI", 12, "bold"), width=12, bg="#4CAF50", fg="white").pack(side=LEFT, padx=15)
        Button(button_frame, text="Giải mã", command=self.decrypt,
               font=("Segoe UI", 12, "bold"), width=12, bg="#2196F3", fg="white").pack(side=LEFT, padx=15)
        Button(button_frame, text="Xóa", command=self.clear_fields,
               font=("Segoe UI", 12, "bold"), width=12,bg="#f44336", fg="white").pack(side=LEFT, padx=10)
        Button(button_frame, text="Lưu", command=self.save_history,
               font=("Segoe UI", 12, "bold"), width=12, bg="#FF9800", fg="white").pack(side=LEFT, padx=10)

    # ====== Xử lý nút ======
    def encrypt(self):
        text = self.input_text.get()
        key = self.key_entry.get()

        if not text or not key:
            self._set_result("⚠️ Vui lòng nhập đầy đủ văn bản và khóa!")
            return

        try:
            result = encrypt_playfair(text, key)
            self._set_result(result)
        except Exception as e:
            self._set_result(f"Lỗi: {str(e)}")

    def decrypt(self):
        text = self.input_text.get()
        key = self.key_entry.get()

        if not text or not key:
            self._set_result("⚠️ Vui lòng nhập đầy đủ văn bản và khóa!")
            return

        try:
            result = decrypt_playfair(text, key)
            self._set_result(result)
        except Exception as e:
            self._set_result(f"Lỗi: {str(e)}")
    
    def clear_fields(self):
        """Làm sạch tất cả ô nhập và kết quả"""
        self.key_entry.delete(0, END)
        self.input_text.delete(0, END)
        self._set_result("")

    def _set_result(self, text):
        """Cập nhật Entry readonly kết quả"""
        self.result_entry.config(state="normal")
        self.result_entry.delete(0, END)
        self.result_entry.insert(0, text)
        self.result_entry.config(state="readonly")

    def save_history(self, algo_type="PlayFair"):
        text = self.input_text.get()
        key = self.key_entry.get()

        # Lấy giá trị từ Entry readonly
        self.result_entry.config(state="normal")
        result = self.result_entry.get()
        self.result_entry.config(state="readonly")

        if not text or not key or not result:
            self._set_result("⚠️ Không có dữ liệu để lưu!")
            return

        # ======= HỘP NHẬP TÊN TÙY CHỈNH =======
        dialog = Toplevel(self)
        dialog.title("Nhập tên bản ghi")
        dialog.configure(bg="#f0f0f0")
        dialog.resizable(False, False)

        w, h = 420, 200
        self.update_idletasks()
        x = self.winfo_rootx() + (self.winfo_width() - w) // 2
        y = self.winfo_rooty() + (self.winfo_height() - h) // 2
        dialog.geometry(f"{w}x{h}+{x}+{y}")
        dialog.grab_set()  # Khóa focus

        Label(dialog, text="Vui lòng nhập tên cho bản ghi:", 
              font=("Segoe UI", 12), bg="#f0f0f0").pack(pady=15)

        name_var = StringVar()
        entry = Entry(dialog, textvariable=name_var, font=("Segoe UI", 12), width=35, justify="center")
        entry.pack(pady=5)
        entry.focus()

        btn_frame = Frame(dialog, bg="#f0f0f0")
        btn_frame.pack(pady=15)

        def confirm():
            name = name_var.get().strip()
            if not name:
                Label(dialog, text="⚠️ Vui lòng nhập tên!", 
                      font=("Segoe UI", 10), fg="red", bg="#f0f0f0").pack()
            else:
                dialog.destroy()
                self._save_to_file(name, text, key, result, algo_type)

        Button(btn_frame, text="Lưu", command=confirm,
               font=("Segoe UI", 11, "bold"), bg="#4CAF50", fg="white", width=10).pack(side=LEFT, padx=10)
        Button(btn_frame, text="Hủy", command=dialog.destroy,
               font=("Segoe UI", 11, "bold"), bg="#f44336", fg="white", width=10).pack(side=LEFT, padx=10)

    def _save_to_file(self, name, text, key, result, algo_type):
        """Lưu dữ liệu lịch sử ra file"""
        history_file = os.path.join("data", "history.json")
        os.makedirs(os.path.dirname(history_file), exist_ok=True)

        if os.path.exists(history_file):
            with open(history_file, "r", encoding="utf-8") as f:
                try:
                    history = json.load(f)
                except json.JSONDecodeError:
                    history = []
        else:
            history = []

        history.append({
            "name": name,
            "text": text,
            "key": key,
            "result": result,
            "type": algo_type,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        with open(history_file, "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=4)

        self._set_result("✅ Đã lưu lịch sử thành công!")
