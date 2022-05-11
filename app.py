import streamlit as st
import sqlite3
import random

def add_blanks(word, sentence, blank = "__"):
  return sentence.replace(word, blank)

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def check_answer(item, answer):
  return item == answer

def form_callback(questions):
    for idx, items in enumerate(questions):
        st.write(check_answer(items[1], answers[idx]))
    # st.session_state.questions = questions
    # st.session_state.form_submit = True
    # for k, v in st.session_state.items():
    #     st.write(k, v)

if "form_submit" not in st.session_state: 
    conn = sqlite3.connect('vocabulary.db')
    c = conn.cursor()

    units_list = []
    for item in c.execute("SELECT DISTINCT unit FROM vocab"):
        units_list.append(item[0])

    st.title("Sentence Completion")
    st.selectbox('Select a unit.', units_list, key='unit')
    st.selectbox('How many question do you want?', [5,10,15,20], key='num_q')

    unit = st.session_state.unit
    num_q = st.session_state.num_q
    input_tup = (unit, num_q)

    st.header(unit)

    st.write("Complete the sentences with the words from the word bank.")

    questions = []
    word_bank = []

    query = "SELECT * FROM vocab WHERE unit = ? ORDER BY RANDOM() LIMIT ?"

    for idx, item in enumerate(c.execute(query, input_tup)):
        word = item[2]
        word_bank.append(word)
        sentence = item[4]
        questions.append((idx, word, sentence, add_blanks(word, sentence)))

    st.subheader("Word Bank")
    random.shuffle(word_bank)
    st.table(chunker(word_bank, 5))

    with st.form("sentence_completion"):
        for q in questions:
            st.text_input(f'{q[0] + 1}. {q[3]}', key=q[0], placeholder="Type answer here")
        submitted = st.form_submit_button(label="Submit", on_click=form_callback, args=(questions,))
        if submitted:
            st.write("Submitted")
    conn.close()
    