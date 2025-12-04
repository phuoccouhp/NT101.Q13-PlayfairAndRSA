from .utils import is_prime, modinv
import random
from math import gcd

def generate_prime(bits=16):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num


def generate_keys(bits=16):
    p = generate_prime(bits)
    q = generate_prime(bits)

    while q == p:
        q = generate_prime(bits)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    if gcd(e, phi) != 1:
        e = 3
        while gcd(e, phi) != 1:
            e += 2

    d = modinv(e, phi)

    public_key = (n, e)
    private_key = (n, d)

    return public_key, private_key, p, q


def generate_keys_from_pq(p, q):
    if not is_prime(p) or not is_prime(q):
        raise Exception("p hoặc q không phải số nguyên tố!")

    if p == q:
        raise Exception("p và q không được bằng nhau!")

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    if gcd(e, phi) != 1:
        e = 3
        while gcd(e, phi) != 1:
            e += 2

    d = modinv(e, phi)

    return (n, e), (n, d)




