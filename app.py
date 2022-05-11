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

questions = []

query = "SELECT * FROM vocab WHERE unit = ? ORDER BY RANDOM() LIMIT ?"

for idx, item in enumerate(c.execute(query, input_tup)):
    word = item[2]
    sentence = item[4]
    questions.append((idx + 1, word, sentence, add_blanks(word, sentence)))

for q in questions:
    st.write(f'{q[0]}. {q[4]}')
    
conn.close()