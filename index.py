from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Encryption function
def encrypt(plaintext, public_key):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(plaintext.encode())
    return ciphertext

# Decryption function
def decrypt(ciphertext, private_key):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode()

# Example usage
public_key = open('public.pem', 'r').read()  # Load public key from file
private_key = open('private.pem', 'r').read()  # Load private key from file

plaintext = "Hello, RSA encryption!"
ciphertext = encrypt(plaintext, public_key)
print("Ciphertext:", ciphertext)

decrypted_text = decrypt(ciphertext, private_key)
print("Decrypted Text:", decrypted_text)
