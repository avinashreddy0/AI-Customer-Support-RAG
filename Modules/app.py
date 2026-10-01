import streamlit as st
from indexing import indexing_file
from retrieval import retrieval_file
from LLM import generation_answer
from prompt import prompt_template

st.set_page_config(page_title='AI Customer Support',page_icon='🛃')

st.header("AI Customer Support.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.write(message['content'])

question = st.chat_input('Any Thing')



if question:
    documents = retrieval_file(question)

    final_prompt = prompt_template(question,documents)

    answer = generation_answer(final_prompt)

    with st.chat_message('user'):
        st.write(question)

    st.session_state.messages.append({
        'role':'user',
        'content':question
    })


    with st.chat_message("assistant"):
        with st.spinner("Thinking"):
            st.write(answer)
    st.session_state.messages.append({
        'role':'assistant',
        'content':answer
    })

    with st.sidebar:
        st.write(documents)
  


    



    

