import os
import sys
import streamlit as st
import time
from langchain.chat_models import AzureChatOpenAI
from langchain.chains import LLMChain, ConversationChain, RetrievalQA
from langchain.embeddings import OpenAIEmbeddings
sys.path.append(os.path.join(os.getcwd()))
from prompts.templateprompt import prompt
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain.vectorstores import Chroma, FAISS
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv()) 

llm = AzureChatOpenAI(
    openai_api_base=os.getenv("OPENAI_API_BASE"),
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_type=os.getenv("OPENAI_API_TYPE"),
    deployment_name=os.getenv("OPENAI_DEPLOYMENT_NAME"),
    openai_api_version=os.getenv("OPENAI_DEPLOYMENT_VERSION"),
    temperature=0.7,
    max_retries=1,
    max_tokens=50)


# embedding
embedding = OpenAIEmbeddings(
    model="text-embedding-ada-002",
    deployment=os.getenv("EMBEDDING_DEPLOYMENT_NAME"),
    openai_api_type="azure",
    chunk_size=1
)

# um modelo de Chain usando LLMChain, tem outro que podemos usar...  Tem que ser o de busca.
llm_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True
)

# Outro modelo de Chain
llm_chain_conversation = ConversationChain(llm=llm, verbose=False, memory=ConversationBufferMemory(), prompt=prompt)


# Modelo de Retrieval, pra ler documentos.

class ChatbotHandler:
    def __init__(self, max_messages=2):
        self.max_messages = max_messages
        if "user_messages" not in st.session_state:
            st.session_state.user_messages = []
        if "document_messages" not in st.session_state:
            st.session_state.document_messages = []

    def display_user_messages(self):
        user_messages_to_display = st.session_state.user_messages[-self.max_messages:]
        for message in user_messages_to_display:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    def display_document_messages(self):
        document_messages_to_display = st.session_state.document_messages[-self.max_messages:]
        for message in document_messages_to_display:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    def process_user_input(self, user_input):
        if user_input:
            start_time = time.time()
            st.chat_message("user").markdown(user_input)
            st.session_state.user_messages.append({"role": "user", "content": user_input})

            with st.spinner("Estamos trabalhando..."):
                response = llm_chain_conversation(user_input)
                elapsed_time = time.time() - start_time
            # Exibindo resposta do Chatbot e tempo de resposta
            st.chat_message("assistant").markdown(f"**Chatbot:** {response['response']}")
            st.session_state.user_messages.append({"role": "assistant", "content": response['response']})
            
            st.success(f"Tempo de resposta: {elapsed_time:.2f} segundos")

        # Limitar o número de mensagens armazenadas
        st.session_state.user_messages = st.session_state.user_messages[-self.max_messages:]

    def process_document_input(self, user_input, chunks):
        if user_input:
            start_time = time.time()
            st.chat_message("user").markdown(user_input)
            st.session_state.document_messages.append({"role": "user", "content": user_input})
            with st.spinner("Estamos trabalhando..."):
                #
                vectordb = FAISS.from_documents(chunks, embedding)
                qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectordb.as_retriever(), memory=ConversationBufferMemory())
                elapsed_time = time.time() - start_time
                response = qa.run(user_input)
            st.chat_message("assistant").markdown(f"**Chatbot:** {response}")
            st.session_state.document_messages.append({"role": "assistant", "content": response})
            st.success(f"Tempo de resposta: {elapsed_time:.2f} segundos")

        # Limitar o número de mensagens armazenadas
        st.session_state.document_messages = st.session_state.document_messages[-self.max_messages:]
