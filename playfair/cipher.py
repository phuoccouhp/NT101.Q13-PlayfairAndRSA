# playfair/cipher.py
from .utils import prepare_text, generate_key_matrix, find_position

def encrypt_playfair(plaintext, keyword, size=5):
    """
    Encrypt plaintext using Playfair cipher
    Returns tuple: (ciphertext, list_of_added_x_positions)
    size = 5 -> 5x5 (chỉ chữ)
    size = 6 -> 6x6 (chữ + số)
    """
    plaintext = prepare_text(plaintext, size)
    matrix = generate_key_matrix(keyword, size)
    pairs = []
    added_x_positions = []  # ghi lại vị trí X chèn

    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        if i + 1 < len(plaintext):
            b = plaintext[i + 1]
            if size == 5 and a == b:
                b = 'X'
                added_x_positions.append(i+1)  # lưu vị trí X chèn
                i += 1
            else:
                i += 2
        else:
            # Nếu lẻ, thêm X padding cho 5x5
            if size == 5:
                b = 'X'
                added_x_positions.append(i+1)
            else:
                b = None
            i += 1
        pairs.append((a, b))

    ciphertext = ""
    n = size
    for a, b in pairs:
        if b is None:
            b = a  # 6x6 lẻ thì copy ký tự cuối
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        if row_a == row_b:
            ciphertext += matrix[row_a][(col_a + 1) % n]
            ciphertext += matrix[row_b][(col_b + 1) % n]
        elif col_a == col_b:
            ciphertext += matrix[(row_a + 1) % n][col_a]
            ciphertext += matrix[(row_b + 1) % n][col_b]
        else:
            ciphertext += matrix[row_a][col_b]
            ciphertext += matrix[row_b][col_a]

    return ciphertext, added_x_positions


def decrypt_playfair(ciphertext, keyword, size=5, added_x_positions=None):
    """
    Decrypt ciphertext using Playfair cipher
    added_x_positions: danh sách vị trí X đã thêm khi mã hóa
    """
    ciphertext = prepare_text(ciphertext, size)
    matrix = generate_key_matrix(keyword, size)
    n = size

    # padding nếu lẻ
    if len(ciphertext) % 2 != 0:
        if size == 5:
            ciphertext += 'X'
        else:
            ciphertext += ciphertext[-1]

    pairs = [(ciphertext[i], ciphertext[i+1]) for i in range(0, len(ciphertext), 2)]
    plaintext = []

    for a, b in pairs:
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        if row_a == row_b:
            plaintext.append(matrix[row_a][(col_a - 1) % n])
            plaintext.append(matrix[row_b][(col_b - 1) % n])
        elif col_a == col_b:
            plaintext.append(matrix[(row_a - 1) % n][col_a])
            plaintext.append(matrix[(row_b - 1) % n][col_b])
        else:
            plaintext.append(matrix[row_a][col_b])
            plaintext.append(matrix[row_b][col_a])

    # Loại bỏ X theo vị trí đã lưu
    if added_x_positions:
        for pos in sorted(added_x_positions, reverse=True):
            if pos < len(plaintext) and plaintext[pos] == 'X':
                del plaintext[pos]

    # Nếu X cuối (padding 5x5)
    if size == 5 and plaintext and plaintext[-1] == 'X':
        plaintext.pop()

    return "".join(plaintext)
