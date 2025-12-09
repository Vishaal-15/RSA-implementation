import math

def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError("modular inverse does not exist")
    return x % m

p = 17
q = 11
e = 7
m = 88

if p == q:
    raise ValueError("p and q must be distinct")

n = p * q
phi = (p - 1) * (q - 1)

if not (1 < e < phi) or math.gcd(e, phi) != 1:
    raise ValueError("invalid e")

try:
    d_priv = pow(e, -1, phi)
except TypeError:
    d_priv = modinv(e, phi)

if not (0 <= m < n):
    raise ValueError("invalid message")

c = pow(m, e, n)
m_decrypted = pow(c, d_priv, n)
print("THe first prime number is :",p)
print("THe second prime number is :",q)
print(phi, d_priv)
print("Encrypted message:", c)
print("Decrypted message:", m_decrypted)
