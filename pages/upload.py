import streamlit as st
import numpy as np
import pandas as pd

from pages.utils import *

# @st.cache
def app():

    '''delete form_submit to run quiz maker on return to page'''
    if st.session_state.form_submit:
        del st.session_state.form_submit

    st.markdown("## Upload Data")

    # Code to read a single file 
    uploaded_file = st.file_uploader("Choose a file", type = ['csv', 'xlsx'])
    if uploaded_file is not None:
        try:
            data = pd.read_csv(uploaded_file)
        except Exception as e:
            print(e)
            data = pd.read_excel(uploaded_file)
    
    if st.button("Load Data"):
        st.markdown("### Uploaded Data")
        st.write("\n")
        st.dataframe(data)
        # data.to_csv('data/main_data.csv', index=False)