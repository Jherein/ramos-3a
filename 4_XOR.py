import streamlit as st

st.header('XOR CIPHER', divider='rainbow')

plaintext = bytes(st.text_input().encode())
key = bytes(st.text_input().encode())