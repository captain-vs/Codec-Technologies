from cryptography.fernet import Fernet


# Function to generate a key and write it to a file
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key


# Function to load the key from the file
def load_key():
    return open("secret.key", "rb").read()


# Function to encrypt a message
def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message


# Function to decrypt a message
def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message


if __name__ == "__main__":
    generate_key()
    key = load_key()

    # Example message
    message = "This is a secret message."

    # Encrypt the message
    encrypted_message = encrypt_message(message, key)
    print(f"Encrypted Message: {encrypted_message}")

    # Decrypt the message
    decrypted_message = decrypt_message(encrypted_message, key)
    print(f"Decrypted Message: {decrypted_message}")
