import streamlit as st
import sqlite3
import random
import datetime

# Custom imports
from pages.utils import *

st.markdown("## Join")

with st.form("join_form"):
    first_name = form.text_input("First Name")
    last_name = form.text_input("Last Name")
    user_name = form.text_input("User Name")
    password1 = form.text_intput("Password", type="password")
    password2 = form.text_input("Confirm Password", type="password")
    submitted = form.form_submit_button("Submit")
if password1.strip() != password2.strip():
    st.warning("The passwords do not match.")