import streamlit as st
import hashlib
import pandas as pd


st.header("Welcome to BLAKE2!🔐")
st.header('BLAKE2', divider='rainbow')

on = st.toggle("Show History")

if on:
    st.write("")

def compute_blake2(input_string):
    # Create a BLAKE2 hash object
    blake2_hash = hashlib.blake2b()

    # Update the hash object with the input string
    blake2_hash.update(input_string.encode('utf-8'))

    # Get the hexadecimal representation of the hash value
    hex_digest = blake2_hash.hexdigest()

    return hex_digest

genre = st.radio(
    "Choose Input",
    [":rainbow[Text]", "File"])

if genre == ':rainbow[Text]':
    st.write('You selected Text.')
    input_string = st.text_area('Plaintext', placeholder="Input Text...")
    button = st.button("Submit", type="primary")

    if button:
        if input_string:  # Check if input_string is not empty
            st.write("Input Text:", input_string)
            blake2_hash = compute_blake2(input_string)
            st.write("BLAKE2 hash of '{}' is: {}".format(input_string, blake2_hash))
        else:
            st.warning("Please input text for BLAKE2 hash to work!")

elif genre == 'File':
    st.write('You selected File.')
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # Read file contents as string
        file_contents = uploaded_file.getvalue().decode("utf-8")
        st.write("File contents:", file_contents)

        # Compute BLAKE2 hash of file contents
        blake2_hash = compute_blake2(file_contents)
        st.write("BLAKE2 hash of file contents:", blake2_hash)
        
else:
    st.write("Please choose.")




