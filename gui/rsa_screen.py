# gui/rsa_screen.py
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from rsa.keygen import generate_keys
from rsa.cipher import encrypt, decrypt
import json
import os
from datetime import datetime

class RSAScreen(Frame):
    def __init__(self, master, controller=None):
        super().__init__(master, bg="#d9d9d9")

        # ===== Tiêu đề =====
        Label(self, text="Mã hóa và giải mã RSA", bg="#d9d9d9", fg="black",
              font=("Segoe UI", 18, "bold")).pack(pady=20)

        # ===== Frame chính =====
        content = Frame(self, bg="#d9d9d9")
        content.pack(pady=10)

        # Văn bản đầu vào
        Label(content, text="Văn bản:", bg="#d9d9d9", font=("Segoe UI", 12)).grid(row=0, column=0, sticky=E, padx=10, pady=8)
        self.input_text = Entry(content, width=50, font=("Segoe UI", 12))
        self.input_text.grid(row=0, column=1, pady=8)

        # Khóa công khai
        Label(content, text="Khóa công khai:", bg="#d9d9d9", font=("Segoe UI", 12)).grid(row=1, column=0, sticky=E, padx=10, pady=8)
        self.public_key_text = Entry(content, width=50, font=("Segoe UI", 12))
        self.public_key_text.grid(row=1, column=1, pady=8)

        # Khóa riêng
        Label(content, text="Khóa riêng:", bg="#d9d9d9", font=("Segoe UI", 12)).grid(row=2, column=0, sticky=E, padx=10, pady=8)
        self.private_key_text = Entry(content, width=50, font=("Segoe UI", 12))
        self.private_key_text.grid(row=2, column=1, pady=8)

        # Kết quả (Entry readonly để có thể copy)
        Label(content, text="Kết quả:", bg="#d9d9d9", font=("Segoe UI", 12)).grid(row=3, column=0, sticky=E, padx=10, pady=8)
        self.result_label = Entry(content, width=50, font=("Segoe UI", 12), justify="center",
                                  state="readonly", fg="blue", readonlybackground="white")
        self.result_label.grid(row=3, column=1, pady=8)

        # ===== Frame chứa các nút =====
        button_frame = Frame(self, bg="#d9d9d9")
        button_frame.pack(pady=15)

        Button(button_frame, text="Tạo khóa", command=self.generate_keys,
               font=("Segoe UI", 12, "bold"), width=12, bg="#4CAF50", fg="white").pack(side=LEFT, padx=10)
        Button(button_frame, text="Mã hóa", command=self.encrypt_text,
               font=("Segoe UI", 12, "bold"), width=12, bg="#2196F3", fg="white").pack(side=LEFT, padx=10)
        Button(button_frame, text="Giải mã", command=self.decrypt_text,
               font=("Segoe UI", 12, "bold"), width=12, bg="#FF9800", fg="white").pack(side=LEFT, padx=10)
        Button(button_frame, text="Lưu", command=self.save_history,
               font=("Segoe UI", 12, "bold"), width=12, bg="#f44336", fg="white").pack(side=LEFT, padx=10)
        Button(button_frame, text="Xóa", command=self.clear_all,
               font=("Segoe UI", 12, "bold"), width=12, bg="#9E9E9E", fg="white").pack(side=LEFT, padx=10)

        # Lưu khóa hiện tại
        self.public_key = None
        self.private_key = None

    # ===== Các chức năng =====
    def generate_keys(self):
        pub, priv = generate_keys(bits=16)
        self.public_key = pub
        self.private_key = priv

        # Hiển thị không dấu ngoặc
        self.public_key_text.delete(0, END)
        self.public_key_text.insert(0, f"{pub[0]}, {pub[1]}")

        self.private_key_text.delete(0, END)
        self.private_key_text.insert(0, f"{priv[0]}, {priv[1]}")

    def encrypt_text(self):
        plaintext = self.input_text.get()
        try:
            if self.public_key_text.get().strip():
                public_key = tuple(map(int, self.public_key_text.get().strip().split(",")))
            elif self.public_key:
                public_key = self.public_key
            else:
                raise Exception("Chưa có khóa công khai")

            cipher = encrypt(plaintext, public_key)

            # Loại bỏ dấu [] khi hiển thị
            if isinstance(cipher, list):
                cipher_str = ", ".join(map(str, cipher))
            else:
                cipher_str = str(cipher)

            # Cập nhật Entry readonly
            self.result_label.config(state="normal")
            self.result_label.delete(0, END)
            self.result_label.insert(0, cipher_str)
            self.result_label.config(state="readonly")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def decrypt_text(self):
        try:
            if self.private_key_text.get().strip():
                private_key = tuple(map(int, self.private_key_text.get().strip().split(",")))
            elif self.private_key:
                private_key = self.private_key
            else:
                raise Exception("Chưa có khóa riêng")

            # Nhận input là chuỗi "12, 34, 56"
            cipher_input = [int(x.strip()) for x in self.input_text.get().strip().split(",")]
            plaintext = decrypt(cipher_input, private_key)

            self.result_label.config(state="normal")
            self.result_label.delete(0, END)
            self.result_label.insert(0, plaintext)
            self.result_label.config(state="readonly")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    # ===== Lưu lịch sử giống PlayFair =====
    def save_history(self):
        text = self.input_text.get()
        key = f"Public: {self.public_key_text.get()}, Private: {self.private_key_text.get()}"

        self.result_label.config(state="normal")
        result = self.result_label.get().strip()
        self.result_label.config(state="readonly")

        if not text or not key or not result:
            self.result_label.config(state="normal")
            self.result_label.delete(0, END)
            self.result_label.insert(0, "⚠️ Không có dữ liệu để lưu!")
            self.result_label.config(state="readonly")
            return

        dialog = Toplevel(self)
        dialog.title("Nhập tên bản ghi")
        dialog.configure(bg="#f0f0f0")
        dialog.resizable(False, False)

        w, h = 420, 200
        self.update_idletasks()
        x = self.winfo_rootx() + (self.winfo_width() - w) // 2
        y = self.winfo_rooty() + (self.winfo_height() - h) // 2
        dialog.geometry(f"{w}x{h}+{x}+{y}")
        dialog.grab_set()

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
                self._save_to_file(name, text, key, result, "RSA")

        Button(btn_frame, text="Lưu", command=confirm,
               font=("Segoe UI", 11, "bold"), bg="#4CAF50", fg="white", width=10).pack(side=LEFT, padx=10)
        Button(btn_frame, text="Hủy", command=dialog.destroy,
               font=("Segoe UI", 11, "bold"), bg="#f44336", fg="white", width=10).pack(side=LEFT, padx=10)

    def _save_to_file(self, name, text, key, result, algo_type):
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

        self.result_label.config(state="normal")
        self.result_label.delete(0, END)
        self.result_label.insert(0, "✅ Đã lưu lịch sử thành công!")
        self.result_label.config(state="readonly")

    # ===== Xóa tất cả =====
    def clear_all(self):
        self.input_text.delete(0, END)
        self.public_key_text.delete(0, END)
        self.private_key_text.delete(0, END)
        self.result_label.config(state="normal")
        self.result_label.delete(0, END)
        self.result_label.config(state="readonly")
        self.public_key = None
        self.private_key = None
