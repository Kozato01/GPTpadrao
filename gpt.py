# PRIMEIRO, MELHORAR MAIS

import streamlit as st
import sys
import os 
import time
from layout.visual_page import set_app_style
import streamlit.components.v1 as components
sys.path.append(os.path.join(os.getcwd()))
from utils.ingest import DocumentChunker
from dotenv import load_dotenv


load_dotenv()

# instancia de Chunker

#chunker = DocumentChunker(chunk_size=1000, chunk_overlap=100)

def main():

    st.title("THE CHAT 😎",anchor=False)
    st.write("##")
    document = st.file_uploader('Arquivo:', label_visibility='collapsed')
    if "messages" not in st.session_state:
        st.session_state.messages = []
    user_input = st.chat_input("")
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])    


    if user_input:
        start_time = time.time()
        st.chat_message("user", avatar="🧑‍💻").markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.spinner("Estamos trabalhando..."):
            #response = gpt_instance._execute('1438', 'l6812', user_input)
            elapsed_time = time.time() - start_time
        #st.chat_message("assistant", avatar="🤖").markdown(f"**Chatbot:** {response['message']}")
        #st.session_state.messages.append({"role": "assistant", "content": response['message']})
        st.success(f"Tempo de resposta: {elapsed_time:.2f} segundos")

    st.text("")  


    


if __name__ == "__main__":
    set_app_style()
    main()
