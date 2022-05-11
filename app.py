import streamlit as st
import sqlite3



conn = sqlite3.connect('vocabulary.db')
c = conn.cursor()

units_list = []
for item in c.execute("SELECT DISTINCT unit FROM vocab"):
  units_list.append(item[0])

st.selectbox('Select a unit.', units_list, key='unit')
unit = st.session_state.unit
unit_tup = (unit,)

st.title(unit)

for row in c.execute("SELECT * FROM vocab WHERE unit = ? LIMIT 10", unit_tup):
    st.write(row[2])

conn.close()