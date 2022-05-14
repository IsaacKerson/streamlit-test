import streamlit as st
import pandas as pd
import numpy as np

from st_aggrid import AgGrid, GridOptionsBuilder, JsCode

def app():
    df_template = pd.DataFrame(
        '',
        index=range(10),
        columns=list('abcde')
    )

    with st.form('example form') as f:
        st.header('Example Form')
        response = AgGrid(df_template, editable=True, fit_columns_on_grid_load=True)
        st.form_submit_button()

    st.write(response['data'])