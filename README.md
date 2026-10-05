RSA Implementation in Python

Two small Python scripts that show RSA encryption in two ways: a from-scratch walkthrough of the math with toy numbers, and a proper RSA-OAEP example using PyCryptodome.

Contents
RSA.py: textbook RSA from first principles (educational)

Walks through the RSA steps with small fixed numbers (p = 17, q = 11, e = 7, message 88):

Computes n = p * q and φ(n) = (p - 1)(q - 1)
Computes the private exponent d as the modular inverse of e mod φ(n), using Python's pow(e, -1, phi) with a fallback to an extended Euclidean algorithm (egcd / modinv)
Checks that p and q are distinct, that gcd(e, φ) = 1, and that the message is smaller than n
Encrypts with c = m^e mod n and decrypts with m = c^d mod n

Run:

bash
python RSA.py
rsa_with_OAEP.py: RSA-OAEP with PyCryptodome
Generates a 2048-bit RSA key pair
Reads text from the user, encrypts it with RSA-OAEP (PKCS1_OAEP) and prints the ciphertext in Base64
Decrypts the ciphertext and prints the recovered text

Run:

bash
pip install pycryptodome
python rsa_with_OAEP.py
Security notes
RSA.py is for learning only. It uses tiny primes, so it is trivially breakable, and it applies no padding. Textbook RSA is deterministic (the same message always gives the same ciphertext) and is vulnerable to well-known attacks. It also does not generate keys: the primes are hardcoded.
OAEP adds randomized padding, so encrypting the same text twice gives different ciphertexts. Use a vetted library such as PyCryptodome for anything real, never hand-written RSA.
With PyCryptodome's defaults (SHA-1 inside OAEP), a 2048-bit key can encrypt at most 214 bytes at a time. Larger data is normally encrypted with a symmetric cipher (for example AES), with RSA protecting only the symmetric key.
Keys in rsa_with_OAEP.py are generated fresh on each run and are not saved.
Limitations and next steps
 Random prime generation with a Miller–Rabin primality test, so RSA.py generates real keys
 Larger key sizes and a side-by-side demo of why unpadded RSA is insecure
 Automated tests against published test vectors
 Key export and import (PEM)
 Hybrid encryption example (RSA-OAEP + AES) for messages longer than the OAEP limit
Tech stack

Python · PyCryptodome

Author

Vishaal A K · GitHub
