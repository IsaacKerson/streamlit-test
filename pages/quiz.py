import streamlit as st
import os.path
import sqlite3
import random
import datetime

# Custom imports
from pages.utils import *

def app():

    '''delete form_upload to run quiz maker on return to page'''
    if "form_upload" in st.session_state.keys():
        del st.session_state.form_upload

    DATABASE = db_path('quiz_maker.db')

    def form_callback(questions):

        st.session_state.form_submit = True
        
        num_correct = 0
        session_id = random_session_id()
        student_id = 'UKWN'
        uct_iso = datetime.datetime.utcnow().isoformat()
        insert_tups = []

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
            insert_tup = (student_id, session_id, uct_iso, items[1], items[2], answer, correct_int )
            insert_tups.append(insert_tup)

        c, conn = db_connect(DATABASE)
        c.executemany("INSERT INTO responses VALUES (?, ?, ?, ?, ?, ?, ?)", insert_tups)
        conn.commit()
        conn.close()

        score_val = 100 * num_correct / len(questions)
        st.metric(label="Final Score", value=f"{score_val}%")
        
    if "form_submit" not in st.session_state:

        c, conn = db_connect(DATABASE)

        st.markdown("# Sentence Completion")
        st.text_input('Comma seperated tags. (Maximum 3)', key='tags')
        st.selectbox('How many question do you want?', [5,10,15,20], key='num_q')
        
        tag_string = st.session_state.tags
        num_q = st.session_state.num_q
        
        clean_tags = clean_string(tag_string)
        terms = split_string(clean_tags)
        subquery = make_subquery(terms)
        query = make_query(subquery, limit = num_q)

        if tag_string:

            questions = []
            word_bank = []

            for idx, item in enumerate(c.execute(query)):
                word = item[0]
                word_bank.append(word)
                sentence = item[2]
                questions.append((idx, word, sentence, add_blanks(word, sentence)))
            
            conn.close()
            
            if len(questions) == 0:
                st.warning("There are no tags that matched that query.")
            elif len(questions) < num_q:
                st.warning(f"There are only {len(questions)} with that tag.")
            else:
                st.markdown(f"## QUIZ: {' '.join(terms)}")
                st.markdown("### Word Bank")
                random.shuffle(word_bank)
                st.table(chunker(word_bank, 5))
                st.markdown("### Questions")
                st.write("Complete the sentences with the words from the word bank.")

                with st.form("sentence_completion"):
                    for q in questions:
                        st.text_input(f'{q[0] + 1}. {q[3]}', key=q[0], placeholder="Type answer here")
                    st.form_submit_button(label="Submit", on_click=form_callback, args=(questions,))
                        