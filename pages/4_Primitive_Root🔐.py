import streamlit as st
from nav import navi

st.set_page_config(
        page_title="Primitive Root",
        page_icon="🔐",
        layout="wide"
    )

navi()

st.header("Welcome to Primitive Root!🔐")
st.header('PRIMITIVE ROOT', divider='rainbow')

def is_prime(modulus):
    if (modulus) < 2:
        return False
    for i in range(2, int(modulus**0.5) + 1):
        if modulus % i == 0:
            return False
    return True
        
def is_primitive(base, modulus):
    powers = set()
    result = 1
    
    for i in range(1, modulus):
        result = (result * base) % modulus
        powers.add(result)
        st.write(f"{base}^{i} mod {modulus} = {result}", end=', ' if i < modulus - 1 else ' ')
        
        if result == 1:
            break
           
    if powers == set(range(1, modulus)):
        st.write(f"==> {base} is primitive root of {modulus},")
        return True
    st.write()
    return False
        
def main():
    modulus = int(st.number_input('Modulus', value=0, placeholder="Must be a prime number..."))
    g = int(st.number_input('Primitive', value=0, placeholder="Inter a valid number..."))

    if not modulus or not g:
        st.warning("Please enter valid values for Modulus and Primitive.")
        return
    
    s_button = st.button('Submit', type='primary')
    if s_button:
        if not is_prime(modulus):
            st.warning(f"{modulus} is not a prime number!!") 
        else:
            primitive_roots = []
            for base in range(1, modulus):
                if is_primitive(base, modulus):
                    primitive_roots.append(base)
                    
            if g in primitive_roots:
                st.write(f"{g} is primitive root: True", primitive_roots)
            else:
                st.write(f"{g} is NOT primitive root of {modulus} - List of Primitive roots:", primitive_roots)
            
if __name__ == '__main__':
    main()






