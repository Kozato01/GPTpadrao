# Definitivo, melhorar alguns coisas e implementar mais.
import streamlit as st
import sys
import os 
import tempfile
import pandas as pd
import time
from layout.visual_page import set_app_style
import streamlit.components.v1 as components
sys.path.append(os.path.join(os.getcwd()))
from utils.ingest import DocumentChunker
from utils.gpt_utils import llm_chain, ChatbotHandler
from dotenv import load_dotenv



load_dotenv()


# instancia de Chunker
chunker = DocumentChunker(chunk_size=1000, chunk_overlap=80)
chatbot_handler = ChatbotHandler(max_messages=5)

def main():
    category = st.sidebar.radio("Escolha a categoria:", ["Conversar com Chatbot", "Add Vectorstore", "Desenvolvimento"])

    set_app_style(category)

    
    if category == "Conversar com Chatbot":
        st.title("THE CHAT 😎",anchor=False)
        st.write("##")
        user_input = st.chat_input("Você diz:")
        chatbot_handler.display_user_messages()
        chatbot_handler.process_user_input(user_input)

#@@@@@@@@
        #@@@@@@@@
        #@@@@@@@@
    elif category == "Add Vectorstore":
        st.title("Chat-Vector", anchor=False)
        st.write("##")
        uploaded_file = st.file_uploader('Arquivo:', )
        if uploaded_file is not None:
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(uploaded_file.read())
            st.sidebar.subheader("Visualização dos Chunks")
            try:
                if uploaded_file.type == "application/pdf":
                    chunks = chunker.chunk_pdf(temp_file.name)
                elif uploaded_file.type == "text/csv":
                    df = pd.read_csv(temp_file.name)
                    st.dataframe(df)
                    chunks = chunker.chunk_csv(temp_file.name)
                else:
                    chunks = chunker.chunk_word_document(temp_file.name)

                st.sidebar.write(chunks)
                st.markdown("---")
                user_input = st.chat_input("")
                chatbot_handler.display_document_messages()
                chatbot_handler.process_document_input(user_input, chunks)

            except pd.errors.EmptyDataError:
                st.sidebar.error("Erro: O arquivo CSV está vazio.")
            except Exception as e:
                st.sidebar.error(f"Erro durante o processamento do arquivo: {str(e)}")
            finally:
                os.remove(temp_file.name)
        else:
            st.sidebar.warning("Nenhum arquivo enviado.")



#@@@@@@@@

    elif category == "Desenvolvimento":
        st.title("Prod...",anchor=False)
        st.write("##")
        st.write(
            "<p style='color: #006d77; font-weight: bold; border: 5px solid #006d77; padding: 15px;'>"
            "Estamos trabalhando irmão... mas vamos lá!"
            "</p>",
            unsafe_allow_html=True
        )
        st.video("https://www.youtube.com/watch?v=WfYRts9BBRM&list=RDWfYRts9BBRM&start_radio=1")
    

if __name__ == "__main__":
    main()
