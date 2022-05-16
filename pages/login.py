from pages.utils import db_connect
import streamlit as st
from yaml.loader import SafeLoader

# Custom imports
from multipage import MultiPage
from authenticator import Hasher, Authenticate
from pages.utils import *

def app():

    yamel_path = db_connect('config.yaml')
    st.write(yamel_path)
    
    with open('../config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    hashed_passwords = Hasher(config['credentials']['passwords']).generate()

    authenticator = Authenticate(
        config['credentials']['names'], 
        config['credentials']['usernames'], 
        hashed_passwords,
        config['cookie']['name'], 
        config['cookie']['key'], 
        cookie_expiry_days=30
    )

    # Alternatively you use st.session_state['name'] and
    # st.session_state['authentication_status'] to access the name and
    # authentication_status.

    authenticator.login('Login', 'main')

    if st.session_state['authentication_status']:
        st.write('Welcome *%s*' % (st.session_state['name']))
        st.title('Some content')
    elif st.session_state['authentication_status'] == False:
        st.error('Username/password is incorrect')
    elif st.session_state['authentication_status'] == None:
        st.warning('Please enter your username and password')