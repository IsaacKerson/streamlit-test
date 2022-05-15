import streamlit as st
import sqlite3
import random
import datetime

# Custom imports
from pages.utils import *

def app():

    DATABASE = db_path('quiz_maker.db')
    c, conn = db_connect(DATABASE)
    query = "CREATE TABLE IF NOT EXISTS users(uct_iso, firstname, lastname, username, email, hashed_password)"
    c.execute(query)

    usernames = []
    emails = []
    
    query = "SELECT username, email FROM users"
    for items in c.execute(query):
        usernames.append(items[0])
        emails.append(items[1])

    st.markdown("## Join")

    with st.form("join_form"):
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        user_name = st.text_input("User Name")
        email = st.text_input("Email")
        password1 = st.text_input("Password", type="password")
        password2 = st.text_input("Confirm Password", type="password")
        
        submitted = st.form_submit_button("Submit")

    if submitted and password1.strip() != password2.strip():
        st.warning("The passwords do not match.")
    if user_name in usernames:
        st.warning("This user name already exists.")
    if email in emails:
        st.warning("This email is already being used.")