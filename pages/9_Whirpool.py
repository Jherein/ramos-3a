from Crypto.Hash import SHA256
import streamlit as st

st.header("Welcome to Whirlpool!🔐")
st.header('Whirlpool', divider='rainbow')

on = st.toggle("Show History")

if on:
    st.write("")
    
def compute_whirlpool(input_string):
    # Create a Whirlpool hash object
    whirlpool_hash = SHA256.new()

    # Update the hash object with the input string
    whirlpool_hash.update(input_string.encode('utf-8'))

    # Get the hexadecimal representation of the hash value
    hex_digest = whirlpool_hash.hexdigest()

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
            whirlpool_hash = compute_whirlpool(input_string)
            st.write("Whirlpool hash of '{}' is: {}".format(input_string, whirlpool_hash))
        else:
            st.warning("Please input text for Whirlpool hash to work!")

elif genre == 'File':
    st.write('You selected File.')
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # Read file contents as string
        file_contents = uploaded_file.getvalue().decode("utf-8")
        st.write("File contents:", file_contents)

        # Compute Whirlpool hash of file contents
        whirlpool_hash = compute_whirlpool(file_contents)
        st.write("Whirlpool hash of file contents:", whirlpool_hash)
        
else:
    st.write("Please choose.")
