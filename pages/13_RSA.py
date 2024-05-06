import rsa
import streamlit as st

from nav import navi

st.set_page_config(
        page_title="Simple Substitution Cipher",
        page_icon="🔐",
        layout="wide"
    )

navi()

st.header("Welcome to Simple RSA!🔐")
st.header('RSA', divider='rainbow')

on = st.toggle("Show History")

if on:
    st.write('')

# Generate RSA key pair
(public_key, private_key) = rsa.newkeys(1024)  # You can adjust the key size as needed

# Convert keys to PEM format (optional)
# public_pem = public_key.save_pkcs1().decode('utf-8')
# private_pem = private_key.save_pkcs1().decode('utf-8')

# # Print public and private keys (optional)
# st.write("Public Key:\n", public_pem)
# st.write("Private Key:\n", private_pem)

# Message to be encrypted
message = st.text_area('Enter your text:')
btn = st.radio('Choose', options=('Encrypt', 'Decrypt'))

if btn == 'Encrypt':        
        # Encrypt message using the recipient's public key
        encrypted_message = rsa.encrypt(message.encode('utf-8'), public_key)
        st.write("Encrypted Message:", encrypted_message)
elif btn == 'Decrypt':
        # Decrypt the encrypted message using the private key
        ciphertext = st.text_input('Enter the ciphertext to decrypt')

        encrypted_message = rsa.encrypt(message.encode('utf-8'), public_key)
        decrypted_message = rsa.decrypt(encrypted_message, private_key)
        btn_submit = st.button('Submit')
        if btn_submit:
            st.write("Original Message:", message)
            st.write("Decrypted Message:", decrypted_message.decode('utf-8'))
