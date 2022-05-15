import streamlit as st
import numpy as np
import pandas as pd
import csv

from pages.utils import *

def app():

    '''delete form_submit to run quiz maker on return to page'''
    if "form_submit" in st.session_state.keys():
        del st.session_state.form_submit
    
    def upload_callback(num_items):
        st.session_state.form_upload = True
        
        input_tups = []

        for idx in range(num_items):
            st.write(st.session_state[f'{word_}{str(idx)}'])

    if "form_upload" not in st.session_state:
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
            st.markdown("### Confirm the data is correct.")
            num_items = 0
            form = st.form("data_check_form")
            with open("data.csv", "r") as f:
                reader = csv.reader(f, delimiter=",")
                for i, line in enumerate(reader):
                    if i == 0:
                        pass
                    else:
                        num_items += 1
                        form.markdown(f"### {i}")
                        form.text_input("Word or Phrase", f"{line[0]}", key=f"word_{i}")
                        form.text_input("Definition", f"{line[1]}", key=f"def_{i}")
                        form.text_input("Example", f"{line[2]}", key=f"ex_{i}")
                        form.text_input("Tags", f"{line[3]}", key=f"tag_{i}")
            form.form_submit_button("Confirm", on_click=upload_callback, args=(num_items))
    # st.text_input(f'{q[0] + 1}. {q[3]}', key=q[0], placeholder="Type answer here")
    # st.form_submit_button(label="Submit", on_click=form_callback, args=(questions,))