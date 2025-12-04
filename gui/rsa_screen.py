import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

from rsa.cipher import encrypt, decrypt
from rsa.keygen import generate_keys, generate_keys_from_pq
from rsa.utils import modinv, gcd


class RSAScreen(Frame):
    def __init__(self, master, controller=None):
        super().__init__(master, bg="#f4f4f4")

        # ===== BIẾN LƯU TRẠNG THÁI =====
        self.current_tab = "encrypt"
        self.public_key = None
        self.private_key = None
        self.newline_positions = []


        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # ================== TIÊU ĐỀ ==================
        title = Label(
            self,
            text="RSA",
            bg="#f4f4f4",
            font=("Segoe UI", 22, "bold")
        )
        title.grid(row=0, column=0, columnspan=2, sticky="w", padx=30, pady=(10, 5))

        # ==================== KHUNG TRÁI ==================
        key_frame = LabelFrame(
            self,
            text="KHÓA",
            font=("Segoe UI", 12, "bold"),
            bg="white",
            labelanchor="nw",
            padx=20,
            pady=20
        )
        key_frame.grid(row=1, column=0, sticky="nsew", padx=(20, 10), pady=10)
        key_frame.grid_columnconfigure(0, weight=1)
        key_frame.grid_columnconfigure(1, weight=1)
        key_frame.grid_columnconfigure(2, weight=1)

        # ===== STYLE CHO BUTTON =====
        btn_style = {
            "font": ("Segoe UI", 11, "bold"),
            "relief": "solid",
            "bd": 1,
            "highlightthickness": 0,
            "height": 1,
            "width": 14,
            "cursor": "hand2"
        }

        btn_red_style = btn_style.copy()
        btn_red_style.update({"bg": "#d32f2f", "fg": "white"})

        # ==================== HÀNG NÚT ====================
        Button(key_frame, text="Nhập thủ công", **btn_style,
               command=self.manual_key).grid(row=0, column=0, padx=4, pady=5)
        Button(key_frame, text="Khóa ngẫu nhiên", **btn_style,
               command=self.random_key).grid(row=0, column=1, padx=4, pady=5)
        Button(key_frame, text="Xóa Khóa", **btn_red_style,
               command=self.clear_keys).grid(row=0, column=2, padx=4, pady=5)

        # ===== INPUT p =====
        Label(key_frame, text="Số p:", bg="white", font=("Segoe UI", 11)).grid(row=1, column=0, sticky="w", pady=(10, 2))
        self.p_entry = Entry(key_frame, font=("Segoe UI", 11), bd=1, relief="solid")
        self.p_entry.grid(row=2, column=0, columnspan=3, sticky="ew", ipady=4, pady=2)

        # ===== INPUT q =====
        Label(key_frame, text="Số q:", bg="white", font=("Segoe UI", 11)).grid(row=3, column=0, sticky="w", pady=(10, 2))
        self.q_entry = Entry(key_frame, font=("Segoe UI", 11), bd=1, relief="solid")
        self.q_entry.grid(row=4, column=0, columnspan=3, sticky="ew", ipady=4, pady=2)

        # ===== PUBLIC KEY =====
        Label(key_frame, text="Khóa công khai:", bg="white", font=("Segoe UI", 11)).grid(row=5, column=0, sticky="w", pady=(10, 2))
        self.public_key_text = Entry(key_frame, font=("Segoe UI", 11), bd=1, relief="solid")
        self.public_key_text.grid(row=6, column=0, columnspan=3, sticky="ew", ipady=4, pady=2)

        # ===== PRIVATE KEY =====
        Label(key_frame, text="Khóa bí mật:", bg="white", font=("Segoe UI", 11)).grid(row=7, column=0, sticky="w", pady=(10, 2))
        self.private_key_text = Entry(key_frame, font=("Segoe UI", 11), bd=1, relief="solid")
        self.private_key_text.grid(row=8, column=0, columnspan=3, sticky="ew", ipady=4, pady=2)

        # ===== CHANGE e =====
        Label(key_frame, text="Thay đổi số e:", bg="white", font=("Segoe UI", 11)).grid(row=9, column=0, sticky="w", pady=(10, 2))
        self.e_entry = Entry(key_frame, font=("Segoe UI", 11), bd=1, relief="solid")
        self.e_entry.grid(row=10, column=0, columnspan=2, sticky="ew", ipady=4, pady=5)

        Button(key_frame, text="Sửa e", **btn_style,
               command=self.update_e).grid(row=10, column=2, padx=5)

        # ==================== KHUNG PHẢI ==================
        cipher_frame = LabelFrame(
            self,
            text="MÃ HÓA, GIẢI MÃ",
            font=("Segoe UI", 12, "bold"),
            bg="white",
            labelanchor="nw",
            padx=20,
            pady=20
        )
        cipher_frame.grid(row=1, column=1, sticky="nsew", padx=(10, 20), pady=10)
        cipher_frame.grid_columnconfigure(0, weight=1)
        cipher_frame.grid_columnconfigure(1, weight=0)

        # ================== TAB HEADER ==================
        tab_frame = Frame(cipher_frame, bg="white")
        tab_frame.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 5))
        self.encrypt_tab = Label(tab_frame, text="Mã hóa",
                                 font=("Segoe UI", 11, "bold"), bg="white",
                                 cursor="hand2")
        self.decrypt_tab = Label(tab_frame, text="Giải mã",
                                 font=("Segoe UI", 11), bg="white",
                                 cursor="hand2")
        self.encrypt_tab.grid(row=0, column=0, padx=5, pady=5)
        self.decrypt_tab.grid(row=0, column=1, padx=5, pady=5)
        self.encrypt_tab.bind("<Button-1>", lambda e: self.switch_tab("encrypt"))
        self.decrypt_tab.bind("<Button-1>", lambda e: self.switch_tab("decrypt"))

        # ================= INPUT TEXT =================
        Label(cipher_frame, text="Văn bản gốc:", bg="white", font=("Segoe UI", 11)).grid(row=1, column=0, sticky="w")
        self.input_text = Entry(cipher_frame, font=("Segoe UI", 11), bd=1, relief="solid")
        self.input_text.grid(row=2, column=0, sticky="ew", ipady=4, pady=5)
        self.input_text.config(justify="left")
        Button(cipher_frame, text="Chọn File", **btn_style, command=self.choose_file).grid(row=2, column=1, padx=5)

        # ================== OUTPUT ==================
        self.output_label = Label(cipher_frame, text="Văn bản mã hóa:", bg="white", font=("Segoe UI", 11))
        self.output_label.grid(row=3, column=0, sticky="w")
        self.result_text = Entry(cipher_frame, font=("Segoe UI", 11), bd=1, relief="solid")
        self.result_text.grid(row=4, column=0, sticky="ew", ipady=4, pady=5)
        self.result_text.config(justify="left")
        Button(cipher_frame, text="Lưu File", **btn_style, command=self.save_file).grid(row=4, column=1, padx=5)

        # ================= NÚT XÓA TẤT CẢ =================
        clear_all_frame = Frame(self, bg="#f4f4f4")
        clear_all_frame.grid(row=2, column=1, sticky="se", padx=20, pady=10)
        Button(clear_all_frame, text="Xóa tất cả", **btn_red_style, command=self.clear_all).pack(anchor="e")

        # ================= BUTTONS =================
        action_frame = Frame(cipher_frame, bg="white")
        action_frame.grid(row=5, column=0, columnspan=2, pady=10)
        self.main_action_btn = Button(action_frame, text="Mã hóa", **btn_style, command=self.encrypt_action)
        self.main_action_btn.grid(row=0, column=0, padx=5)
        Button(action_frame, text="Đảo ngược", **btn_style, command=self.reverse_action).grid(row=0, column=1, padx=5)
        Button(action_frame, text="Xóa", **btn_red_style, command=self.clear_cipher).grid(row=0, column=2, padx=5)


    # ======================== CHỨC NĂNG ==========================
    def random_key(self):
        pub, priv, p, q = generate_keys(bits=16)

        self.public_key = pub
        self.private_key = priv

        n, e = pub
        _, d = priv

        self.p_entry.delete(0, END)
        self.q_entry.delete(0, END)
        self.p_entry.insert(0, str(p))
        self.q_entry.insert(0, str(q))

        self.public_key_text.delete(0, END)
        self.public_key_text.insert(0, f"n = {n}, e = {e}")

        self.private_key_text.delete(0, END)
        self.private_key_text.insert(0, f"n = {n}, d = {d}")

        self.e_entry.delete(0, END)

    def manual_key(self):
        try:
            p = int(self.p_entry.get())
            q = int(self.q_entry.get())

            if p <= 1 or q <= 1:
                return messagebox.showerror("Lỗi", "p và q phải là số nguyên tố!")

            if gcd(p, q) != 1:
                return messagebox.showerror("Lỗi", "p và q phải độc lập nhau!")

            pub, priv = generate_keys_from_pq(p, q)

            self.public_key = pub
            self.private_key = priv

            n, e = pub
            _, d = priv

            self.public_key_text.delete(0, END)
            self.public_key_text.insert(0, f"n = {n}, e = {e}")

            self.private_key_text.delete(0, END)
            self.private_key_text.insert(0, f"n = {n}, d = {d}")

        except:
            messagebox.showerror("Lỗi", "Giá trị p hoặc q không hợp lệ!")

    def clear_keys(self):
        self.p_entry.delete(0, END)
        self.q_entry.delete(0, END)
        self.public_key_text.delete(0, END)
        self.private_key_text.delete(0, END)
        self.e_entry.delete(0, END)

        self.public_key = None
        self.private_key = None

    def update_e(self):
        if not self.public_key or not self.private_key:
            return messagebox.showerror("Lỗi", "Chưa có khóa để sửa e!")

        try:
            new_e = int(self.e_entry.get())
            n, _ = self.public_key
            _, d = self.private_key

            p = int(self.p_entry.get())
            q = int(self.q_entry.get())
            phi = (p - 1) * (q - 1)

            if gcd(new_e, phi) != 1:
                return messagebox.showerror("Lỗi", "e mới không hợp lệ!")

            new_d = modinv(new_e, phi)

            self.public_key = (n, new_e)
            self.private_key = (n, new_d)

            self.public_key_text.delete(0, END)
            self.public_key_text.insert(0, f"n = {n}, e = {new_e}")

            self.private_key_text.delete(0, END)
            self.private_key_text.insert(0, f"n = {n}, d = {new_d}")

            self.e_entry.delete(0, END)
            messagebox.showinfo("OK", "Đã cập nhật e mới!")
        except:
            messagebox.showerror("Lỗi", "Giá trị e không hợp lệ!")

    def reverse_action(self):
        result_data = self.result_text.get()

        self.input_text.delete(0, END)
        self.input_text.insert(0, result_data)

        self.result_text.delete(0, END)


    def clear_cipher(self):
        self.input_text.delete(0, END)
        self.result_text.delete(0, END)

    def switch_tab(self, mode):
        self.current_tab = mode

        if mode == "encrypt":
            self.encrypt_tab.config(font=("Segoe UI", 11, "bold"))
            self.decrypt_tab.config(font=("Segoe UI", 11))

            self.output_label.config(text="Văn bản mã hóa:")
            self.main_action_btn.config(text="Mã hóa")
        else:
            self.encrypt_tab.config(font=("Segoe UI", 11))
            self.decrypt_tab.config(font=("Segoe UI", 11, "bold"))

            self.output_label.config(text="Văn bản giải mã:")
            self.main_action_btn.config(text="Giải mã")

    def encrypt_action(self):
        if not self.public_key:
            return messagebox.showerror("Lỗi", "Chưa có khóa công khai!")

        text = self.input_text.get()
        if not text:
            return messagebox.showerror("Lỗi", "Chưa nhập văn bản!")

        try:
            if self.current_tab == "encrypt":
                cipher = encrypt(text, self.public_key)
                result = str(cipher)  
            else:
                cipher = eval(text)  
                result = decrypt(cipher, self.private_key)
        except Exception as e:
            return messagebox.showerror("Lỗi", f"Không thể xử lý: {e}")


        self.result_text.delete(0, END)
        display_result = str(result).replace("\n", " ")
        self.result_text.insert(0, display_result)

    def choose_file(self):
        path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if not path:
            return
        with open(path, "r", encoding="utf-8") as f:
            data = f.read()
        
        self.newline_positions = [i for i, c in enumerate(data) if c == "\n"]
        
        display_data = data.replace("\n", " ")
        self.input_text.delete(0, END)
        self.input_text.insert(0, display_data)

    def restore_newlines(self, text):
        """Chèn ký tự xuống dòng vào các vị trí đã lưu"""
        text_list = list(text)
        for offset, pos in enumerate(self.newline_positions):
            if pos + offset <= len(text_list):
                text_list.insert(pos + offset, "\n")
        return "".join(text_list)

    def save_file(self):
        data = self.result_text.get()
        if not data:
            return messagebox.showerror("Lỗi", "Không có dữ liệu để lưu!")

        data_with_newlines = self.restore_newlines(data)

        path = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text Files", "*.txt")])
        if not path:
            return

        with open(path, "w", encoding="utf-8") as f:
            f.write(data_with_newlines)

        messagebox.showinfo("OK", "Đã lưu file thành công!")

    def clear_all(self):
        self.clear_cipher()   
        self.clear_keys()     
        self.newline_positions = []  