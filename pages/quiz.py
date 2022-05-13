import streamlit as st
import sqlite3
import random
import datetime

# Custom imports
from multipage import MultiPage
from pages.utils import add_blanks, chunker, random_session_id, check_answer

def app():
    DATABASE = '../vocabulary.db'

    def db_connect(database):
        conn = sqlite3.connect(database)
        c = conn.cursor()
        return c, conn

    def form_callback(questions):
        st.session_state.form_submit = True
        num_correct = 0
        session_id = random_session_id()
        student_id = 'UKWN'
        uct_iso = datetime.datetime.utcnow().isoformat()
        st.title("Feedback")
        for idx, items in enumerate(questions):
            answer = st.session_state[idx]
            correct_str = 'incorrect'
            correct_int = 0
            if check_answer(items[1], answer):
                correct_str = 'correct'
                correct_int = 1
                num_correct += 1
                st.success(f"Question {idx + 1}")
            else:
                st.error(f"Question {idx + 1}")
            st.write(f"{items[3]}")
            st.write(f"Answer: {items[1]}")
            st.write(f"Your answer: {answer}")
            st.write(f"You are {correct_str}.")
            insert_tup = (student_id, session_id, uct_iso, items[1], items[2], answer, correct_int, )
            c, conn = db_connect(DATABASE)
            c.execute("INSERT INTO responses VALUES (?, ?, ?, ?, ?, ?, ?)", insert_tup)
        conn.commit()
        conn.close()
        score_val = 100 * num_correct / len(questions)
        st.metric(label="Final Score", value=f"{score_val}%")
        
    if "form_submit" not in st.session_state: 
        c, conn = db_connect(DATABASE)

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
        