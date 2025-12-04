from tkinter import *
from tkinter import ttk, filedialog
from tkinter import messagebox
from playfair.cipher import encrypt_playfair, decrypt_playfair
import random, string

class PlayFairScreen(Frame):
    def __init__(self, master):
        super().__init__(master, bg="#f4f4f4")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.x_positions_enc = []
        self.x_positions_dec = []

        # ====================== TIÊU ĐỀ ======================
        Label(self, text="PlayFair", bg="#f4f4f4", font=("Segoe UI", 22, "bold")).grid(
            row=0, column=0, columnspan=2, sticky="w", padx=30, pady=(10,5)
        )

        # ==================== KHUNG TRÁI (KHÓA) ======================
        key_frame = LabelFrame(
            self, text="KHÓA",
            font=("Segoe UI", 12, "bold"),
            bg="white", labelanchor="nw",
            padx=20, pady=20
        )
        key_frame.grid(row=1, column=0, sticky="nsew", padx=(20,10), pady=10)
        key_frame.grid_columnconfigure(0, weight=1)

        Label(key_frame, text="Từ khóa:", bg="white", font=("Segoe UI", 11)).grid(
            row=0, column=0, sticky="w", pady=(0,5)
        )
        self.key_entry = Entry(key_frame, font=("Segoe UI",11), bd=1, relief="solid")
        self.key_entry.grid(row=1, column=0, sticky="ew", ipady=4)

        # ===== STYLE NÚT =====
        self.btn_style = {
            "font": ("Segoe UI", 11, "bold"),
            "relief": "solid",
            "bd": 1,
            "highlightthickness": 0,
            "height": 1,
            "width": 14,
            "cursor": "hand2"
        }

        self.btn_red_style = self.btn_style.copy()
        self.btn_red_style.update({"bg": "#d32f2f", "fg": "white"})

        btn_frame = Frame(key_frame, bg="white")
        btn_frame.grid(row=2, column=0, sticky="e", pady=10)

        Button(btn_frame, text="Khóa ngẫu nhiên", **self.btn_style, command=self.random_key).grid(row=0,column=0,padx=5)
        Button(btn_frame, text="Xóa khóa", **self.btn_red_style, command=lambda: self.key_entry.delete(0, END)).grid(row=0,column=1,padx=5)

        # ==================== KHUNG PHẢI (MA TRẬN) ======================
        matrix_frame = LabelFrame(
            self, text="MA TRẬN",
            font=("Segoe UI", 12, "bold"),
            bg="white", labelanchor="nw",
            padx=10, pady=10
        )
        matrix_frame.grid(row=1, column=1, sticky="nsew", padx=(10,20), pady=10)
        matrix_frame.grid_columnconfigure(0, weight=1)

        Label(matrix_frame, text="Chế độ ma trận:", bg="white", font=("Segoe UI",11)).grid(row=0,column=0, sticky="w")
        self.matrix_mode = ttk.Combobox(matrix_frame, values=["5 x 5","6 x 6"], state="readonly", font=("Segoe UI",11))
        self.matrix_mode.current(0)
        self.matrix_mode.grid(row=1,column=0, sticky="ew", ipady=3)

        Button(matrix_frame, text="Tạo ma trận", **self.btn_style, command=self.update_matrix_from_key).grid(row=1,column=1,padx=10)

        # Khung chứa ô ma trận
        self.matrix_cells_frame = Frame(matrix_frame, bg="white")
        self.matrix_cells_frame.grid(row=2,column=0, pady=10, columnspan=2)

        # ================= KHUNG MÃ HÓA - GIẢI MÃ =================
        bottom_frame = LabelFrame(self, text="MÃ HÓA - GIẢI MÃ", font=("Segoe UI",12,"bold"),
                                  bg="white", labelanchor="nw", padx=20, pady=10)
        bottom_frame.grid(row=2,column=0,columnspan=2, sticky="nsew", padx=20, pady=(0,10))
        bottom_frame.grid_columnconfigure(0, weight=1)
        bottom_frame.grid_rowconfigure(1, weight=1)

        notebook = ttk.Notebook(bottom_frame)
        notebook.grid(row=0,column=0, sticky="nsew", pady=5)

        tab_encrypt = Frame(notebook, bg="white")
        tab_decrypt = Frame(notebook, bg="white")
        notebook.add(tab_encrypt, text="Mã hóa")
        notebook.add(tab_decrypt, text="Giải mã")

        # =================== TAB MÃ HÓA =======================
        tab_encrypt.grid_columnconfigure(0, weight=50)
        tab_encrypt.grid_columnconfigure(1, weight=1)

        Label(tab_encrypt, text="Văn bản:", bg="white", font=("Segoe UI",11)).grid(row=0,column=0, sticky="w")
        self.input_encrypt = Entry(tab_encrypt, font=("Segoe UI",11), bd=1, relief="solid")
        self.input_encrypt.grid(row=1,column=0, sticky="ew", ipady=4, pady=5)
        Button(tab_encrypt, text="Chọn File", **self.btn_style, command=lambda: self.choose_file(self.input_encrypt)).grid(row=1,column=1,padx=5, sticky="e")

        Label(tab_encrypt, text="Kết quả:", bg="white", font=("Segoe UI",11)).grid(row=2,column=0, sticky="w")
        self.output_encrypt = Entry(tab_encrypt, font=("Segoe UI",11), bd=1, relief="solid", fg="black")
        self.output_encrypt.grid(row=3,column=0, sticky="ew", ipady=4, pady=5)
        Button(tab_encrypt, text="Lưu File", **self.btn_style, command=lambda: self.save_file(self.output_encrypt)).grid(row=3,column=1,padx=5, sticky="e")

        action_frame_enc = Frame(tab_encrypt, bg="white")
        action_frame_enc.grid(row=4,column=0,columnspan=3, sticky="e", pady=10)
        Button(action_frame_enc, text="Mã hóa", **self.btn_style, command=self.encrypt).grid(row=0,column=0,padx=5)
        Button(action_frame_enc, text="Đảo ngược", **self.btn_style, command=lambda:self.reverse_output(self.input_encrypt,self.output_encrypt)).grid(row=0,column=1,padx=5)
        Button(action_frame_enc, text="Xóa", **self.btn_red_style, command=lambda:self.clear_tab(self.input_encrypt,self.output_encrypt)).grid(row=0,column=2,padx=5)

        # =================== TAB GIẢI MÃ =======================
        tab_decrypt.grid_columnconfigure(0, weight=50)
        tab_decrypt.grid_columnconfigure(1, weight=1)
        Label(tab_decrypt, text="Văn bản:", bg="white", font=("Segoe UI",11)).grid(row=0,column=0, sticky="w")
        self.input_decrypt = Entry(tab_decrypt, font=("Segoe UI",11), bd=1, relief="solid")
        self.input_decrypt.grid(row=1,column=0, sticky="ew", ipady=4, pady=5)
        Button(tab_decrypt, text="Chọn File", **self.btn_style, command=lambda: self.choose_file(self.input_decrypt)).grid(row=1,column=1,padx=5, sticky="e")

        Label(tab_decrypt, text="Kết quả:", bg="white", font=("Segoe UI",11)).grid(row=2,column=0, sticky="w")
        self.output_decrypt = Entry(tab_decrypt, font=("Segoe UI",11), bd=1, relief="solid", fg="black")
        self.output_decrypt.grid(row=3,column=0, sticky="ew", ipady=4, pady=5)
        Button(tab_decrypt, text="Lưu File", **self.btn_style, command=lambda: self.save_file(self.output_decrypt)).grid(row=3,column=1,padx=5, sticky="e")

        action_frame_dec = Frame(tab_decrypt, bg="white")
        action_frame_dec.grid(row=4,column=0,columnspan=3, sticky="e", pady=10)
        Button(action_frame_dec, text="Giải mã", **self.btn_style, command=self.decrypt).grid(row=0,column=0,padx=5)
        Button(action_frame_dec, text="Đảo ngược", **self.btn_style, command=lambda:self.reverse_output(self.input_decrypt,self.output_decrypt)).grid(row=0,column=1,padx=5)
        Button(action_frame_dec, text="Xóa", **self.btn_red_style, command=lambda:self.clear_tab(self.input_decrypt,self.output_decrypt)).grid(row=0,column=2,padx=5)

        # ================= NÚT XÓA TẤT CẢ DƯỚI CÙNG BÊN PHẢI =================
        clear_all_frame = Frame(self, bg="#f4f4f4")
        clear_all_frame.grid(row=3, column=1, sticky="e", padx=20, pady=(0,20))
        Button(clear_all_frame, text="Xóa tất cả", **self.btn_red_style, command=self.clear_all).pack(anchor="e")

    # ====================== CHỨC NĂNG ======================

    def tokenize_text(self, raw):
        tokens = []
        buffer = ""

        def flush_buffer():
            nonlocal buffer
            if buffer:
                tokens.append((buffer, "word"))
                buffer = ""

        for c in raw:
            if c.isalnum():            
                buffer += c
            else:
                flush_buffer()
                if c == " ":
                    tokens.append((" ", "space"))
                elif c == "\n":
                    tokens.append(("\n", "newline"))
                else:
                    tokens.append((c, "other"))

        flush_buffer()
        return tokens


    def restore_format(self, tokens, encoded_words):
        result = []
        idx = 0
        for tok, typ in tokens:
            if typ == "word":
                result.append(encoded_words[idx])
                idx += 1
            else:
                result.append(tok)
        return "".join(result)
    

    def save_file(self, entry_widget):
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")]
        )
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(entry_widget.get())
            messagebox.showinfo("OK", "Đã lưu file thành công!")

    def choose_file(self, entry_widget):
        path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not path:
            return

        text = None
        for enc in ["utf-8", "utf-16", "cp1252"]:
            try:
                with open(path, "r", encoding=enc) as f:
                    text = f.read()
                break
            except:
                continue

        if text is None:
            messagebox.showerror("Lỗi", "Không thể đọc file!")
            return

        self.tokens_encrypt = self.tokenize_text(text)
        entry_widget.delete(0, END)
        entry_widget.insert(0, text)

    def clear_tab(self, inp, out):
        inp.delete(0, END)
        out.delete(0, END)

    def clear_all(self):
        self.key_entry.delete(0, END)
        self.input_encrypt.delete(0, END)
        self.output_encrypt.delete(0, END)
        self.input_decrypt.delete(0, END)
        self.output_decrypt.delete(0, END)
        for widget in self.matrix_cells_frame.winfo_children():
            widget.destroy()


    # ================= MÃ HÓA - GIẢI MÃ ====================
    def encrypt(self):
        key = self.key_entry.get()
        raw_text = self.input_encrypt.get()
        mode = self.matrix_mode.get()
        size = 5 if mode == "5 x 5" else 6

        if not key or not raw_text:
            self.output_encrypt.delete(0, END)
            self.output_encrypt.insert(0, "Thiếu dữ liệu!")
            return


        self.tokens_encrypt = self.tokenize_text(raw_text)

        words = [tok for tok, t in self.tokens_encrypt if t == "word"]

        joined = "".join(words)

        matrix = self.generate_matrix(key, size * size)
        valid, invalid_char = self.validate_input(joined, matrix)
        if not valid:
            self.output_encrypt.delete(0, END)
            self.output_encrypt.insert(
                0, f"Ký tự '{invalid_char}' không hợp lệ với ma trận {mode}!")
            return

        cipher, x_pos = encrypt_playfair(joined, key, size=size)
        self.x_positions_enc = x_pos

        encoded_words = []
        idx = 0
        for tok, typ in self.tokens_encrypt:
            if typ == "word":
                length = len(tok)
                encoded_words.append(cipher[idx:idx + length])
                idx += length

        final = self.restore_format(self.tokens_encrypt, encoded_words)

        self.output_encrypt.delete(0, END)
        self.output_encrypt.insert(0, final)


    def decrypt(self):
        key = self.key_entry.get()
        raw_text = self.input_decrypt.get()
        mode = self.matrix_mode.get()
        size = 5 if mode == "5 x 5" else 6

        if not key or not raw_text:
            self.output_decrypt.delete(0, END)
            self.output_decrypt.insert(0, "Thiếu dữ liệu!")
            return

        self.tokens_decrypt = self.tokenize_text(raw_text)
        words = [tok for tok, t in self.tokens_decrypt if t == "word"]
        joined = "".join(words)

        matrix = self.generate_matrix(key, size * size)
        valid, invalid_char = self.validate_input(joined, matrix)
        if not valid:
            self.output_decrypt.delete(0, END)
            self.output_decrypt.insert(
                0, f"Ký tự '{invalid_char}' không hợp lệ với ma trận {mode}!")
            return

        plain = decrypt_playfair(joined, key, size=size,
                                 added_x_positions=self.x_positions_enc)

        decoded_words = []
        idx = 0
        for tok, typ in self.tokens_decrypt:
            if typ == "word":
                length = len(tok)
                decoded_words.append(plain[idx:idx + length])
                idx += length

        final = self.restore_format(self.tokens_decrypt, decoded_words)

        self.output_decrypt.delete(0, END)
        self.output_decrypt.insert(0, final)


    def reverse_output(self, input_widget, output_widget):
        text_out = output_widget.get()

        input_widget.delete(0, END)
        input_widget.insert(0, text_out)

        output_widget.delete(0, END)


        if input_widget == self.input_encrypt:
            self.input_decrypt.delete(0, END)
            self.input_decrypt.insert(0, text_out)

            self.output_decrypt.delete(0, END)
        
        else:
            self.input_encrypt.delete(0, END)
            self.input_encrypt.insert(0, text_out)

            self.output_encrypt.delete(0, END)

    def validate_input(self, text, matrix):
        size = len(matrix)
        allowed_chars = set()
        if size == 25:
            allowed_chars = set("abcdefghiklmnopqrstuvwxyz")  
        else:
            allowed_chars = set("abcdefghijklmnopqrstuvwxyz0123456789")
        for ch in text.lower().replace("j",""): 
            if ch.isalnum() and ch not in allowed_chars:
                return False, ch
        return True, ""

    # ================= MA TRẬN PLAYFAIR ====================
    def generate_matrix(self, key, size):
        key = key.lower().replace("j","")
        matrix=[]
        used=set()
        for ch in key:
            if ch.isalnum() and ch not in used:
                used.add(ch)
                matrix.append(ch)
        alphabet = "abcdefghiklmnopqrstuvwxyz" if size==25 else "abcdefghijklmnopqrstuvwxyz0123456789"
        for ch in alphabet:
            if ch not in used:
                used.add(ch)
                matrix.append(ch)
        return matrix

    def show_matrix(self, matrix, size):
        for widget in self.matrix_cells_frame.winfo_children():
            widget.destroy()
        n = 5 if size==25 else 6
        index = 0
        for r in range(n):
            for c in range(n):
                Label(self.matrix_cells_frame, text=matrix[index].upper(),
                      width=3, height=1, font=("Segoe UI",10,"bold"),
                      bd=1, relief="solid", bg="white").grid(row=r,column=c,padx=1,pady=1)
                index +=1

    def update_matrix_from_key(self):
        key = self.key_entry.get()
        mode = self.matrix_mode.get()
        size = 25 if mode=="5 x 5" else 36
        matrix = self.generate_matrix(key, size)
        self.show_matrix(matrix, size)

    def random_key(self):
        letters = string.ascii_lowercase.replace("j","")
        key = "".join(random.sample(letters,10))
        self.key_entry.delete(0, END)
        self.key_entry.insert(0,key)
