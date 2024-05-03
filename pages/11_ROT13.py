import streamlit as st

def rot13_encrypt(text):
    encrypted_text = ""
    for char in text:
        if 'a' <= char <= 'z':
            encrypted_text += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            encrypted_text += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def rot13_decrypt(text):
    decrypted_text = ""
    for char in text:
        if 'a' <= char <= 'z':
            decrypted_text += chr((ord(char) - ord('a') - 13) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            decrypted_text += chr((ord(char) - ord('A') - 13) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

# Example usage:
plaintext = st.text_area('Plaintext')
st.write("Original plaintext:", plaintext)

# Encrypt plaintext using ROT13
encrypted_text = rot13_encrypt(plaintext)
st.write("Encrypted ciphertext:", encrypted_text)

# Decrypt ciphertext using ROT13
decrypted_text = rot13_decrypt(encrypted_text)
st.write("Decrypted plaintext:", decrypted_text)
