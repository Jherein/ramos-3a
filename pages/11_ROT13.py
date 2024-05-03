import streamlit as st

from nav import navi

st.set_page_config(
        page_title="Reverse Cipher",
        page_icon="🔐",
        layout="wide"
    )

navi()

st.header("Welcome to ROT13!🔐")
st.header('ROT13', divider='rainbow')

on = st.toggle("Show History")

if on:
    st.write('')

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

genre = st.selectbox(
    "What type of content do you want?",
    ["Text", "File"])

if genre == 'Text':
    plaintext = st.text_input('Enter a plaintext')
    option = st.radio('Choose process', options=('Encrypt', 'Decrypt'))

    if option == 'Encrypt':
        btn = st.button('Submit', type='primary')
        if btn:
            if not plaintext:
                st.warning('Please enter a text to encrypt!')
            else:
                # Encrypt plaintext using Reverse Cipher
                ciphertext = rot13_encrypt(plaintext)
                st.write("Encrypted Plaintext:", ciphertext)

    elif option == 'Decrypt':
                # Decrypt plaintext using Reverse Cipher
                ciphertext = st.text_input('Enter the ciphertext to decrypt')
                decrypted_plaintext = rot13_decrypt(ciphertext)
                btn = st.button('Submit', type='primary')
                if btn:
                    if not ciphertext:
                        st.warning('Please input a text to decrypt!')
                    else:
                        st.write("Decrypted Ciphertext:", decrypted_plaintext)
           
elif genre == 'File':
    st.write('You selected File.')
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # Read file contents as string
        file_contents = uploaded_file.getvalue().decode("utf-8")
        st.write("File contents:", file_contents)

        # Compute Reverse Cipher of file contents
        radio = st.radio("Choose process", options=("Encypt", "Decrypt"))

        if radio == 'Encypt':
            cipher_reverse = rot13_encrypt(file_contents)
            radio_btn = st.button('Submit', type='primary')
            if radio_btn:
                st.write("Encrypted File:", cipher_reverse)
        elif radio == 'Decrypt':
            ciphertext = st.text_input('Enter the ciphertext to decrypt')
            decipher_reverse = rot13_decrypt(ciphertext)
            btn = st.button('Submit', type='primary')
            if btn:
                    if not ciphertext:
                        st.warning('Please input a text to decrypt!')
                    else:
                        st.write("Decrypted Ciphertext:", decipher_reverse)
        
else:
    st.write("Please choose.")
