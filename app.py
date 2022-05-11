import streamlit as st
import sqlite3

def add_blanks(word, sentence, blank = "__"):
  return sentence.replace(word, blank)

conn = sqlite3.connect('vocabulary.db')
c = conn.cursor()

units_list = []
for item in c.execute("SELECT DISTINCT unit FROM vocab"):
  units_list.append(item[0])

st.selectbox('Select a unit.', units_list, key='unit')
st.selectbox('How many question do you want?', [5,10,15,20], key='num_q')
unit = st.session_state.unit
num_q = st.session_state.num_q
input_tup = (unit, num_q)

st.title(unit)

for idx, item in enumerate(c.execute("SELECT * FROM vocab WHERE unit = ? LIMIT ?", input_tup)):
    word = item[2]
    sentence = item[4]
    st.write(f'{idx + 1}. {add_blanks(word, sentence)}')

conn.close()