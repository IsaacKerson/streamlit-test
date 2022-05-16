from pickle import FALSE
from pages.utils import empty
import streamlit as st
import sqlite3
import datetime

# Custom imports
from pages.utils import *
from authenticator import Hasher

def app():

    drop_table = False

    DATABASE = db_path('quiz_maker.db')
    c, conn = db_connect(DATABASE)

    if drop_table:
        st.write("User Table Dropped.")
        query = "DROP TABLE IF EXISTS users"
        c.execute(query)

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

    if empty(first_name) or empty(last_name) or empty(user_name) or \
        empty(email) or empty(password1) or empty(password2):
        st.warning("Complete all inputs.")
    elif submitted and password1.strip() != password2.strip():
        st.warning("The passwords do not match.")
    elif user_name in usernames:
        st.warning("This user name already exists.")
    elif email in emails:
        st.warning("This email is already being used.")
    else:
        uct_iso = datetime.datetime.utcnow().isoformat()
        hashed_password = Hasher(password1).generate()
        st.write(firstname, lastname, username, email, hashed_password)
        query = "INSERT INTO users(uct_iso, firstname, lastname, username, email, hashed_password) VALUES(?, ?, ?, ?, ?, ?)"
        c.execute(query, (uct_iso, first_name, last_name, user_name, email, hashed_password))
        conn.commit()
        conn.close()
        st.success("You have joined.")