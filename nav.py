import streamlit as st

def navi():
    # columns = st.columns((1,1,1,1))
    columns1 = st.columns((1, 1, 1, 1))
    columns2 = st.columns((1, 1, 1, 1))

    # with columns[0]:
    #     st.page_link("pages/2_XOR_Cipher🔐.py", label="XOR Cipher", icon="🗝️", use_container_width=True)
    # with columns[1]:
    #     st.page_link("pages/3_Caesar_Cipher🔐.py", label="Caesar Cipher", icon="🗝️", use_container_width=True)
    # with columns[2]:
    #     st.page_link("pages/4_Primitive_Root🔐.py", label="Primitive Root", icon="🗝️", use_container_width=True)
    # with columns[3]:
    #     st.page_link("pages/5_Block_Cipher🔐.py", label="Block Cipher", icon="🗝️", use_container_width=True)
    with columns1[0]:
        st.page_link("pages/6_MD5_Hash🔐.py", label="MD5", icon="🗝️", use_container_width=True)
    with columns1[1]:
        st.page_link("pages/7_Sha1🔐.py", label="SHA1", icon="🗝️", use_container_width=True)
    with columns1[2]:
        st.page_link("pages/8_Blake2🔐.py", label="BLAKE2", icon="🗝️", use_container_width=True)
    with columns1[3]:
        st.page_link("pages/9_RIPEMD-160🔐.py", label="RIPEMD-160", icon="🗝️", use_container_width=True)

    st.markdown('---')
    with columns2[0]:
        st.page_link("pages/10_Reverse_Cipher🔐.py", label="Reverse Cipher", icon="🗝️", use_container_width=True)
    with columns2[1]:
        st.page_link("pages/11_ROT13🔐.py", label="ROT13", icon="🗝️", use_container_width=True)
    with columns2[2]:
        st.page_link("pages/12_Simple_Substitution_Cipher🔐.py", label="Simple Substitution Cipher", icon="🗝️", use_container_width=True)
    with columns2[3]:
        st.page_link("pages/13_RSA🔐.py", label="RSA", icon="🗝️", use_container_width=True)

