from playfair.utils import prepare_text, generate_key_matrix, find_position

def encrypt_playfair(plaintext, keyword):
    plaintext = prepare_text(plaintext)
    matrix = generate_key_matrix(keyword)
    pairs = []

    # Ghép cặp 2 ký tự
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        if i + 1 < len(plaintext):
            b = plaintext[i + 1]
            if a == b:
                b = 'X'
                i += 1
            else:
                i += 2
        else:
            b = 'X'
            i += 1
        pairs.append((a, b))

    ciphertext = ""
    for a, b in pairs:
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)

        if row_a == row_b:
            # Cùng hàng
            ciphertext += matrix[row_a][(col_a + 1) % 5]
            ciphertext += matrix[row_b][(col_b + 1) % 5]
        elif col_a == col_b:
            # Cùng cột
            ciphertext += matrix[(row_a + 1) % 5][col_a]
            ciphertext += matrix[(row_b + 1) % 5][col_b]
        else:
            # Hình chữ nhật
            ciphertext += matrix[row_a][col_b]
            ciphertext += matrix[row_b][col_a]

    return ciphertext


def decrypt_playfair(ciphertext, keyword):
    """
    Giải mã PlayFair và loại bỏ các ký tự 'X' filler/padding:
    - Nếu có mẫu A X A trong plaintext giải mã được, ký tự 'X' ở giữa sẽ bị xóa (được coi là filler).
    - Nếu ký tự cuối cùng là 'X', coi là padding và xóa.
    Trả về plaintext đã 'clean'.
    """
    ciphertext = prepare_text(ciphertext)
    matrix = generate_key_matrix(keyword)

    # đảm bảo độ dài chẵn (nếu lẻ, thêm 'X' — nhưng thông thường ciphertext hợp lệ là chẵn)
    if len(ciphertext) % 2 != 0:
        ciphertext = ciphertext + "X"

    pairs = [(ciphertext[i], ciphertext[i + 1]) for i in range(0, len(ciphertext), 2)]

    plaintext = []
    for a, b in pairs:
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)

        if row_a == row_b:
            # Cùng hàng -> dịch trái 1
            plaintext.append(matrix[row_a][(col_a - 1) % 5])
            plaintext.append(matrix[row_b][(col_b - 1) % 5])
        elif col_a == col_b:
            # Cùng cột -> dịch lên 1
            plaintext.append(matrix[(row_a - 1) % 5][col_a])
            plaintext.append(matrix[(row_b - 1) % 5][col_b])
        else:
            # Hình chữ nhật -> đổi cột
            plaintext.append(matrix[row_a][col_b])
            plaintext.append(matrix[row_b][col_a])

    # plaintext hiện là list ký tự; join để xử lý cleanup
    plain = "".join(plaintext)

    # ===== Cleanup: loại bỏ 'X' được chèn làm filler (A X A -> A A) =====
    cleaned = []
    i = 0
    L = len(plain)
    while i < L:
        # Nếu gặp pattern LETTER, 'X', SAME LETTER -> bỏ 'X'
        if i + 2 < L and plain[i+1] == 'X' and plain[i] == plain[i+2]:
            cleaned.append(plain[i])
            # bỏ plain[i+1] (là 'X'), tiếp tục từ plain[i+2]
            i += 2
        else:
            cleaned.append(plain[i])
            i += 1

    # Nếu còn 1 ký tự ở cuối do vòng lặp (nếu i == L-1) thì nó đã được thêm; kiểm tra xóa padding cuối
    # Lưu ý: nếu ký tự cuối cùng là 'X' rất có thể là padding => bỏ
    if cleaned and cleaned[-1] == 'X':
        cleaned.pop()

    return "".join(cleaned)

