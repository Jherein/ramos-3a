import streamlit as st

st.balloons()
st.header("Welcome to XOR Cipher!")
st.write("What is your name?")

txt_FNAME = st.text_input("First Name:")
txt_LNAME = st.text_input("Last Name:")

btn_submit = st.button("Submit")

if btn_submit:
    # st.error(f"Hello {txt_FNAME} {txt_LNAME}")
    # st.success(f"Hello {txt_FNAME} {txt_LNAME}")
    st.write(f"Hello {txt_FNAME} {txt_LNAME}")


st.header('XOR CIPHER', divider='rainbow')
def xor_encrypt(plaintext, key):
    ciphertext = bytearray()
    for i in range(len(plaintext)):
        plaintext_byte = plaintext[i]
        key_byte = key[i % len(key)]

        xor_result = plaintext_byte ^ key_byte
        st.write('Plaintext byte:', format(plaintext_byte, '08b'), "=", chr(plaintext_byte))
        st.write('Key byte:            ', format(key_byte, '08b'), "=", chr(key_byte))
        st.write('XOR result:    ', format(xor_result, '08b'), "=", chr(xor_result))
        st.write('--------------------')
        ciphertext.append(xor_result)

    return ciphertext

def xor_decrypt(ciphertext, key):

    return xor_encrypt(ciphertext, key)

plaintext = bytes(st.text_input("Plaintext").encode())
key = bytes(st.text_input("Key").encode())

if st.button('Submit'):
    if not key:
        st.error('Input Invalid!')
    else:
        if plaintext == key:
            st.write('Plaintext should not be equal to the key')
        elif len(plaintext.decode()) < len(key.decode()):
            st.write('Plaintext length should be equal or greater than the length of key')
        else:
            encrypted = xor_encrypt(plaintext, key)
            st.write('Ciphertext:', encrypted.decode())

            decrypted = xor_decrypt(encrypted, key)
            st.write('Decrypted:', decrypted.decode()) 
        

