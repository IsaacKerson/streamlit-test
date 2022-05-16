import streamlit as st
import yaml

# Custom imports
from multipage import MultiPage
from authenticator import Hasher, Authenticate
from pages.utils import *

def app():

    yamel_path = db_path('config.yaml')

    with open(yamel_path) as file:
        config = yaml.safe_load(file)

    hashed_passwords = Hasher(config['credentials']['passwords']).generate()

    auth = Authenticate(
        config['credentials']['names'], 
        config['credentials']['usernames'], 
        hashed_passwords,
        config['cookie']['name'], 
        config['cookie']['key'], 
        cookie_expiry_days=30
    )

    auth.login('Login', 'main')

    if st.session_state['authentication_status']:
        auth.logout('Logout', 'main')
        st.title('Some content')
    elif st.session_state['authentication_status'] == False:
        st.error('Username/password is incorrect')
    elif st.session_state['authentication_status'] == None:
        st.warning('Please enter your username and password')