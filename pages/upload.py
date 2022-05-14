import streamlit as st
import numpy as np
import pandas as pd
import csv

from pages.utils import *

def app():

    '''delete form_submit to run quiz maker on return to page'''
    if "form_submit" in st.session_state.keys():
        del st.session_state.form_submit

    st.markdown("## Upload Data")

    # Code to read a single file 
    uploaded_file = st.file_uploader("Choose a file", type = ['csv', 'xlsx'])
    if uploaded_file is not None:
        try:
            data = pd.read_csv(uploaded_file)
            data.to_csv('data.csv', index=False)
        except Exception as e:
            print(e)
            data = pd.read_excel(uploaded_file)
            data.to_csv('data.csv', index=False)
  
    if st.button("Load Data"):
        st.markdown("### Data")
        col1, col2, col3 = st.columns(3)
        with open("data.csv", "r") as f:
            reader = csv.reader(f, delimiter=",")
            for i, line in enumerate(reader):
                if i == 0:
                    col1, col2, col3, col4 = st.columns(4)
                    col1.markdown("**#**")
                    col2.markdown(f"**{reader[0][0]}**")
                    col3.markdown(f"**{reader[0][1]}**")
                    col4.markdown(f"**{reader[0][2]}**")
                else:
                    col1, col2, col3, col4 = st.columns(4)
                    col1.write(f"{i}")
                    col2.write(f"{line[0]}")
                    col3.write(f"{line[1]}")
                    col4.write(f"{line[2]}")