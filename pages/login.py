import streamlit as st
import yaml

# Custom imports
from multipage import MultiPage
from authenticator import Hasher, Authenticate
from pages.utils import *

def app():

    # DATABASE = db_path('quiz_maker.db')
    # c, conn = db_connect(DATABASE)
    # query = "SELECT * FROM users"
    # for item in c.execute(query):
    #     st.write("item")
    # conn.commit()
    # conn.close()

    yamel_path = db_path('config.yaml')

    with open(yamel_path) as file:
        config = yaml.safe_load(file)

    auth = Authenticate(
        config['database']['name'], 
        config['database']['table'],
        config['cookie']['name'], 
        config['cookie']['key'], 
        cookie_expiry_days=30
    )

    st.write(auth.get_path())
    st.write(auth.get_connection())
    st.write(auth.check_connection())

    auth.login('Login', 'main')
    
    st.write(auth.check_username())
    st.write(auth.get_hashed_password())
    st.write(auth.check_pw())
    
    if st.session_state['authentication_status']:
        auth.logout('Logout', 'main')
        st.title('Some content')
    elif st.session_state['authentication_status'] == False:
        st.error('Username/password is incorrect')
    elif st.session_state['authentication_status'] == None:
        st.warning('Please enter your username and password')