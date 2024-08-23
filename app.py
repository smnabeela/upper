import streamlit as st
st.header('Uppercase')
txt = st.text_input('Enter a text')
btn = st.button('Enter')
st.image('island.jpg')
if btn:
    a = txt.upper()
    st.subheader(a)
    
