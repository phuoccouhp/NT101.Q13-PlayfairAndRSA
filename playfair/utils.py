# playfair/utils.py

def prepare_text(text, size=5):
    text = text.lower()
    if size == 5:
        text = text.replace('j','i')
        return ''.join([c for c in text if c.isalpha()])
    else:  # 6x6 -> giữ chữ + số
        return ''.join([c for c in text if c.isalnum()])


def generate_key_matrix(keyword, size=5):
    keyword = prepare_text(keyword, size)
    matrix = []
    used = set()

    for c in keyword:
        if c not in used:
            matrix.append(c)
            used.add(c)

    if size == 5:
        alphabet = "abcdefghiklmnopqrstuvwxyz"  # không có j
    else:
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"

    for c in alphabet:
        if c not in used:
            matrix.append(c)
            used.add(c)

    return [matrix[i:i+size] for i in range(0, size*size, size)]


def find_position(matrix, letter):
    n = len(matrix)
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == letter:
                return row, col
    return None
