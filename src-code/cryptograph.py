from cryptography.fernet import Fernet

#text to encrypt
text = input().encode()
key = Fernet.generate_key()
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(text)
print(cipher_text)
plain_text = cipher_suite.decrypt(cipher_text)