import streamlit as st
st.title("This is an update to the app.")
x = st.slider('Select a value')
st.write(x, 'squared is', x * x)