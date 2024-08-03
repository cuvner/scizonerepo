import streamlit as st
from streamlit_chat import message
from brain import chatbot_brain
from storage import Storage


def main():
    st.markdown("<h1>Adrian Chatb🤖t</h1>", unsafe_allow_html=True)

    if "history" not in st.session_state:
        st.session_state.history = []  # empty chat screen for newly opened app

    message("Hi, how may I help you?")

    with st.sidebar:
        user_question = st.text_input("Ask your question", key="user_input", placeholder="type your question")

    if user_question:
        with st.spinner("Thinking ..."):
            Storage.to_txt(user_question)

            response = chatbot_brain(user_question)

        st.session_state.history.append({"user": user_question, "bot": response})

    if st.session_state.history:
        for index, conversation in enumerate(st.session_state.history):
            # user question - section
            message(conversation["user"], is_user=True, key=str(index) + "_user")
            # bot response - section
            message(conversation["bot"], key=str(index) + "_bot")

if __name__ == "__main__":
    main()
