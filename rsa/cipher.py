def encrypt(text, public_key):
    n, e = public_key

    data_bytes = text.encode("utf-8")

    max_block = (n.bit_length() - 1) // 8
    blocks = [data_bytes[i:i+max_block] for i in range(0, len(data_bytes), max_block)]

    cipher_blocks = []
    for block in blocks:
        m = int.from_bytes(block, byteorder="big")
        c = pow(m, e, n)
        cipher_blocks.append(c)

    return cipher_blocks 

def decrypt(cipher_blocks, private_key):
    n, d = private_key
    data_bytes = b""

    for c in cipher_blocks:
        m = pow(c, d, n)
        block_bytes = m.to_bytes((m.bit_length() + 7) // 8, byteorder="big")
        data_bytes += block_bytes

    return data_bytes.decode("utf-8", errors="ignore")