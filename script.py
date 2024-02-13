import streamlit as st
from langchain.callbacks import get_openai_callback
from langchain.chains import LLMChain, RetrievalQA
from langchain.chat_models import AzureChatOpenAI
from langchain.prompts import ChatPromptTemplate, load_prompt
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma, FAISS
from langchain.llms import AzureOpenAI
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain import PromptTemplate
from langchain.document_loaders import UnstructuredFileLoader
from dotenv import load_dotenv, find_dotenv
import os



load_dotenv(find_dotenv()) # read local .env file

#LLM
llmchat = AzureChatOpenAI(
    openai_api_base=os.getenv("OPENAI_API_BASE"),
    openai_api_version=os.getenv("OPENAI_API_VERSION"),
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_type=os.getenv("OPENAI_API_TYPE"),
    deployment_name=os.getenv("DEPLOYMENT_NAME"),
    temperature=0.9,
    max_retries=1,
    max_tokens=100
)


#prompt template por pasta
promptLoadjson = load_prompt("prompttemplat/prompttemp.json")

#prompt manual
templatemaster = """You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.
Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. 
Please ensure that your responses are socially unbiased and positive in nature.
If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. 
If you don't know the answer to a question, please don't share false information.

Question: {query}

Answer: """


prompt_template = PromptTemplate(
    input_variables=["query"],
    template=templatemaster
)


#Criando as chain (correntes)
llm_chain = LLMChain(
    prompt=prompt_template,
    llm=llmchat,
    verbose=True
)


def count_token(result):
    with get_openai_callback() as cb:
        #result = llm_chain.run(query)
        print(f'Spent a total of {cb.total_tokens} tokens')
        #print(result)
    return result

def get_pdf_text(pdf_file):
    text = ""
    pdf_reader = PdfReader(pdf_file)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


def PDF_READER(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunk = text_splitter.split_text(text)
    return chunk


def main():
    st.title("Bem-vindo ao Chat GPT-3.5!")
    user_input = st.text_input("Digite sua mensagem aqui:")
    result = llm_chain.run(user_input)
    st.write(result)
    with st.sidebar:
        st.subheader("Import PDF")
        pdf_file = st.file_uploader("Faça o upload de um arquivo PDF", type=["pdf"])

    if st.sidebar.button("Process"):
        text = get_pdf_text(pdf_file)
        chunk = PDF_READER(text)
        st.write(chunk)

    
    #doc_seach = Chroma.from(chunk, embeddings)
    #chain = RetrievalQA.from_chain_type(llm=AzureOpenAI(model_kwargs={'engine':'gpt-35-erlacher'}), chain_type='stuff', retriever = doc_seach.as_retriever())
    #st.write(chain.run(user_input))
        

    #st.write(pdf_file)
    """ if user_input:
        st.write(f"Você disse: {user_input}")
        st.write(f"AI disse: {result}")"""





if __name__ == '__main__':
    main()