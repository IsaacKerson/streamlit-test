import streamlit as st
import yaml

# Custom imports
from multipage import MultiPage
from authenticator import Hasher, Authenticate
from pages.utils import *

def app():

    DATABASE = db_path('quiz_maker')
    c, conn = db_connect(DATABASE)
    query = "SELECT * FROM users"
    for item in c.execute(query):
        st.write("item")
    conn.commit()
    conn.close()

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

    print(aut.get_path())
    # auth.login('Login', 'main')

    # if st.session_state['authentication_status']:
    #     auth.logout('Logout', 'main')
    #     st.title('Some content')
    # elif st.session_state['authentication_status'] == False:
    #     st.error('Username/password is incorrect')
    # elif st.session_state['authentication_status'] == None:
    #     st.warning('Please enter your username and password')