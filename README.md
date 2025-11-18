# NT101.Q13-PlayfairAndRSA

Đồ án an toàn mạng máy tính NT101.Q13 về thuật toán Playfair và RSA

# Các chức năng chính

```bash
- mã hóa và giải mã palyfair
- mã hóa và giải mã rsa
- Lưu và xem lịch sử mã hóa và giải mã
- kiếm tra thuật toán trước khi hiển thị
```

# Cây thư mục

```bash
NT101.Q13-PlayfairAndRSA/
│
├── playfair/              # Chứa các module cho thuật toán PlayFair
│ ├── cipher.py            # Hàm/lớp chính để mã hóa và giải mã PlayFair
│ └── utils.py             # Các hàm tiện ích hỗ trợ: xử lý key, chuẩn hóa chuỗi
│
├── rsa/                   # Chứa các module cho thuật toán RSA
│ ├── keygen.py            # Tạo cặp khóa công khai (public) và riêng (private)
│ ├── cipher.py            # Hàm/lớp chính để mã hóa và giải mã RSA
│ └── utils.py             # Hàm tiện ích: kiểm tra số nguyên tố, tính mod, định dạng dữ liệu
│
├── gui/                   # Chứa code giao diện người dùng nếu dùng GUI
│ ├── app.py               # màn hình gốc
│ ├── main_menu.py         # menu
│ ├── history_screen.py    # màn hình lịch sử
│ ├── playfair_screen.py   # màn hình playfair
│ ├── rsa_screen.py        # màn hình rsa
│ └── visuals/             # trực quan hóa thuật toán
│       ├── playfair_visual.py
│       └── rsa_visual.py
│
├── tests/                 # Thư mục kiểm thử (unit test)
│ ├── test_playfair.py     # Test các hàm PlayFair có chạy đúng không
│ └── test_rsa.py          # Test các hàm RSA (mã hóa, giải mã, sinh khóa)
│
├── data/                  # Thư mục lưu file đầu vào/ra
│ └── history.json         # lưu lịch sử mã hóa/giải mã
│
├── resources/             # Lưu icon, ảnh minh họa
│   ├── icons/
│   └── images/
│
├── config/                # cấu hình mặc định
│   └── settings.json
│
└── README.md              # Hướng dẫn cài đặt, chạy ứng dụng, mô tả tính năng
```
