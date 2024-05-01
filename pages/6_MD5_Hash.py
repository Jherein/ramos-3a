import streamlit as st
import hashlib
import pandas as pd
from io import StringIO

st.header("Welcome to MD5!🔐")
st.header('MD5', divider='rainbow')

on = st.toggle("Show History")

if on:
    st.write("MD5 (technically called Message-Digest Algorithm) was invented by Ronald Rivest, but it's only one of his three algorithms. MD5 was released in 1992 and was also built for 32-bit machines. It isn't as fast as MD4 but it is considered to be more secure than the previous MDx implementations.")

def compute_md5(input_string):
    # Create an MD5 hash object
    md5_hash = hashlib.md5()

    # Update the hash object with the input string
    md5_hash.update(input_string.encode('utf-8'))

    # Get the hexadecimal representation of the hash value
    hex_digest = md5_hash.hexdigest()

    return hex_digest

genre = st.radio(
    "Choose Input",
    ["Text", "File"])

if genre == 'Text':
    st.write('You selected Text.')
    input_string = st.text_area('Plaintext', placeholder="Input Text...")
    button = st.button("Submit", type="primary")

    if button:
        if input_string:  # Check if input_string is not empty
            st.write("Input Text:", input_string)
            md5_hash = compute_md5(input_string)
            st.write("MD5 hash of '{}' is: {}".format(input_string, md5_hash))
        else:
            st.warning("Please input text for MD5 hash to work!")

elif genre == 'File':
    st.write('You selected File.')
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # Read file contents as string
        file_contents = uploaded_file.getvalue().decode("utf-8")
        st.write("File contents:", file_contents)

        # Compute MD5 hash of file contents
        md5_hash = compute_md5(file_contents)
        st.write("MD5 hash of file contents:", md5_hash)
        
else:
    st.write("Please choose.")




