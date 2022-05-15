import streamlit as st
import sqlite3
import random
import datetime

# Custom imports
from pages.utils import *

st.markdown("## Join")

with st.form("join_form"):
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    user_name = st.text_input("User Name")
    password1 = st.text_intput("Password", type="password")
    password2 = st.text_input("Confirm Password", type="password")
    
    submitted = st.form_submit_button("Submit")

if submitted and password1.strip() != password2.strip():
    st.warning("The passwords do not match.")