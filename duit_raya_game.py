import streamlit as st
import random

# Soalan dan jawapan
questions = {
    "Berapakah 2 + 3?": ["5", "3", "7"],
    "Apakah warna bendera Malaysia?": ["Merah, Putih, Biru, Kuning", "Hijau, Putih, Merah", "Biru, Hitam, Kuning"],
    "Berapakah jumlah hari dalam setahun?": ["365", "360", "366"],
    "Siapakah bapa kemerdekaan Malaysia?": ["Tunku Abdul Rahman", "Tun Mahathir", "Tun Razak"],
    "Apakah ibu negara Malaysia?": ["Kuala Lumpur", "Putrajaya", "Johor Bahru"]
}

def main():
    st.title("Game Duit Raya untuk GF")
    st.write("Jawab 5 soalan dan kumpulkan duit raya!")
    
    if "duit_raya" not in st.session_state:
        st.session_state.duit_raya = 0
        st.session_state.answered_questions = 0
        st.session_state.current_question = ""
        st.session_state.shuffled_answers = []
    
    if st.session_state.answered_questions < 5:
        if not st.session_state.current_question:
            next_question()
        
        st.write(st.session_state.current_question)
        selected = st.radio("Pilih jawapan:", st.session_state.shuffled_answers)
        
        if st.button("Hantar Jawapan"):
            check_answer(selected)
    else:
        st.write(f"Permainan tamat! Anda telah mengumpul RM{st.session_state.duit_raya}.")
        if st.button("Main Semula"):
            reset_game()

def next_question():
    st.session_state.current_question = random.choice(list(questions.keys()))
    st.session_state.shuffled_answers = random.sample(questions[st.session_state.current_question], 3)
    st.experimental_rerun()

def check_answer(answer):
    if answer == questions[st.session_state.current_question][0]:
        st.session_state.duit_raya += 1  # Tambah RM1 jika betul
        st.success("Betul! Anda dapat RM1.")
    else:
        st.error("Salah! Cuba lagi.")
    
    st.session_state.answered_questions += 1
    st.session_state.current_question = ""
    
    if st.session_state.answered_questions < 5:
        next_question()
    else:
        st.experimental_rerun()

def reset_game():
    st.session_state.duit_raya = 0
    st.session_state.answered_questions = 0
    st.session_state.current_question = ""
    st.session_state.shuffled_answers = []
    next_question()
    
if __name__ == "__main__":
    main()
