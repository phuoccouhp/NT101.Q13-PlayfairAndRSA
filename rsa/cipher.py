def encrypt(message, public_key):
    n, e = public_key
    # chuyển từng ký tự sang số và mã hóa
    cipher = [pow(ord(char), e, n) for char in message]
    return cipher

def decrypt(cipher, private_key):
    n, d = private_key
    message = ''.join([chr(pow(c, d, n)) for c in cipher])
    return message
