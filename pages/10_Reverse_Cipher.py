import streamlit as st

def reverse_cipher(plaintext):
    # Reverse the plaintext
    ciphertext = plaintext[::-1]
    return ciphertext

def reverse_decipher(ciphertext):
    # Reverse the ciphertext to get the original plaintext
    plaintext = ciphertext[::-1]
    return plaintext

genre = st.selectbox(
    "What type of content do you want?",
    ["Text", "File"])

if genre == 'Text':
    plaintext = st.text_input('Enter a plaintext')
    option = st.radio('Choose process', options=('Encrypt', 'Decrypt'))

    if option == 'Encrypt':
        btn = st.button('Submit')
        if btn:
            if not plaintext:
                st.warning('Please enter a text to encrypt!')
            else:
                # Encrypt plaintext using Reverse Cipher
                ciphertext = reverse_cipher(plaintext)
                st.write("Encrypted Plaintext:", ciphertext)

    elif option == 'Decrypt':
            # Decrypt plaintext using Reverse Cipher
            ciphertext = st.text_input('Enter the ciphertext to decrypt')
            decrypted_plaintext = reverse_decipher(ciphertext)
            btn = st.button('Submit')
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
            cipher_reverse = reverse_cipher(file_contents)
            radio_btn = st.button('Submit')
            if radio_btn:
                st.write("Encrypted File:", cipher_reverse)
        elif radio == 'Decrypt':
            ciphertext = st.text_input('Enter the ciphertext to decrypt')
            decipher_reverse = reverse_decipher(ciphertext)
            btn = st.button('Submit')
            if btn:
                    if not ciphertext:
                        st.warning('Please input a text to decrypt!')
                    else:
                        st.write("Decrypted Ciphertext:", decipher_reverse)
        
else:
    st.write("Please choose.")
