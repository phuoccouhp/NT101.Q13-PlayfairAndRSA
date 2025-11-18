def prepare_text(text):
    """
    Làm sạch chuỗi, loại bỏ ký tự không phải chữ cái, viết hoa, và thay J -> I.
    """
    text = ''.join([c.upper() for c in text if c.isalpha()])
    text = text.replace('J', 'I')
    return text


def generate_key_matrix(keyword):
    """
    Tạo ma trận 5x5 từ khóa.
    """
    keyword = prepare_text(keyword)
    matrix = []
    used = set()

    for c in keyword:
        if c not in used:
            matrix.append(c)
            used.add(c)

    for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # Không có J
        if c not in used:
            matrix.append(c)
            used.add(c)

    # Trả về dạng 2D (5x5)
    return [matrix[i:i + 5] for i in range(0, 25, 5)]


def find_position(matrix, letter):
    """
    Tìm tọa độ (row, col) của một ký tự trong ma trận.
    """
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None
