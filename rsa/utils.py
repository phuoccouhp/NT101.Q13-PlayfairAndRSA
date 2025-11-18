import random
from math import gcd

def is_prime(n, k=5):
    """Kiểm tra số nguyên tố (Miller-Rabin)"""
    if n < 2: return False
    for p in [2,3,5,7,11,13,17,19,23,29,31]:
        if n % p == 0: return n == p
    s, d = 0, n-1
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
        a = random.randrange(2, n-1)
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(s-1):
            x = pow(x, 2, n)
            if x == n-1: break
        else:
            return False
    return True

def modinv(a, m):
    """Tìm modulo inverse: a*x ≡ 1 (mod m)"""
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x % m

def extended_gcd(a, b):
    if a == 0: return b, 0, 1
    g, y, x = extended_gcd(b % a, a)
    return g, x - (b//a)*y, y
