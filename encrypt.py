
from cryptography.fernet import Fernet


# string the key in a file
def encrypt():
    # key generation

    global key
    key = Fernet.generate_key()

    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)

    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
    # using the generated key
    fernet = Fernet(key)
    # opening the original file to encrypt
    with open('data.txt', 'rb') as file:
        original = file.read()
    # encrypting the file
    encrypted = fernet.encrypt(original)

    # opening the file in write mode and
    # writing the encrypted data
    with open('data.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)





