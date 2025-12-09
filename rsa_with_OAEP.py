from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

key = RSA.generate(2048)
public_key = key.publickey()

encrypt_cipher = PKCS1_OAEP.new(public_key)
decrypt_cipher = PKCS1_OAEP.new(key)

text = input("Enter text to encrypt: ")
plaintext_bytes = text.encode()

cipher_bytes = encrypt_cipher.encrypt(plaintext_bytes)
cipher_b64 = base64.b64encode(cipher_bytes).decode()

print("\nEncrypted (Base64):")
print(cipher_b64)

decrypted_bytes = decrypt_cipher.decrypt(cipher_bytes)
decrypted_text = decrypted_bytes.decode()

print("\nDecrypted:")
print(decrypted_text)
