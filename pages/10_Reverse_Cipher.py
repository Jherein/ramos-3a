import streamlit as st

def reverse_cipher(plaintext):
    # Reverse the plaintext
    ciphertext = plaintext[::-1]
    return ciphertext

def reverse_decipher(ciphertext):
    # Reverse the ciphertext to get the original plaintext
    plaintext = ciphertext[::-1]
    return plaintext

# Example usage:
plaintext = st.text_input('Enter a plaintext')
st.write("Original plaintext:", plaintext)

# Encrypt plaintext using Reverse Cipher
ciphertext = reverse_cipher(plaintext)
st.write("Encrypted ciphertext:", ciphertext)

# Decrypt ciphertext using Reverse Cipher
decrypted_plaintext = reverse_decipher(ciphertext)
st.write("Decrypted plaintext:", decrypted_plaintext)
