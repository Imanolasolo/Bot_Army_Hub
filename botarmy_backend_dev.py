import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
import os

if 'train' not in st.session_state:
    st.session_state.train = False

def get_pdf_text(pdf_list):
    text = ""
    for pdf in pdf_list:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    if not text_chunks:
        st.warning("Please upload a textual PDF file - this PDF file contains images only.")
        return None
    embeddings = OpenAIEmbeddings(openai_api_key=st.session_state.api_key)
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vector_store):
    llm = ChatOpenAI(openai_api_key=st.session_state.api_key)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory
    )
    return conversation_chain

def handle_user_input(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    # Clear previous messages before showing new messages
    for i, msg in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            col1, col2 = st.columns([1, 12])
            with col1:
                st.image('user_icon.png', width=50)
            with col2:
                st.write(msg.content)
        else:
            col1, col2 = st.columns([1, 12])
            with col1:
                st.image('bot_icon.png', width=50)
            with col2:
                st.write(msg.content)

def homepage():
    st.title("Welcome to BOT ARMY")
    st.markdown("BOT ARMY is a platform for creating Backend projects in various frameworks using LLMs (Large Language Models from PDFs and URLs) as engine.")
    st.markdown("With BOT ARMY, you can easily generate code snippets, project structures, and even interact with ChatGPT to get assistance in your development process.")
    st.markdown("Follow these steps to get started:")
    st.warning("1. Insert your OpenAI API KEY in the sidebar when asked.")
    st.success("2. Choose the type of BOT you want to generate.")
    st.warning("3. Train the agent choosing the selector each time you start the bot.")
    st.success("4. Start creating your Backend project!")
    st.success("5. After using the bot push 'Clear Conversation' on sidebar to clear the messages and work clearly.")

def framework_page(framework, sample_pdf):
    st.title(f"{framework} BOT Page")
    st.warning(f"This is the page for {framework} BOT.")
    
    use_sample_pdf = st.checkbox(f"Talk with {framework} Bot")
    if use_sample_pdf:
        st.session_state.pdf_files = [sample_pdf]
    
    train = st.button("Train the Agent")
    if train:
        with st.spinner("Processing"):
            raw_text = get_pdf_text(st.session_state.pdf_files)
            st.session_state.pdf_text = raw_text
            text_chunks = get_text_chunks(raw_text)
            vector_store = get_vector_store(text_chunks)
            if vector_store:
                st.session_state.conversation = get_conversation_chain(vector_store)
                st.session_state.train = True

    if not st.session_state.train:
        st.warning("First Train the Agent")

    if st.session_state.train:
        st.write("<h5><br>Ask anything from your documents, it doesn’t matter the language I am multi-idiomatic!</h5>", unsafe_allow_html=True)
        user_question = st.text_input(label="", placeholder="Enter something...")
        if user_question:
            handle_user_input(user_question)

def clear_conversation_page():
    st.title("Clear Conversation")
    st.info("Check a bot from sidebar")

# Sidebar actions
st.sidebar.image('Botarmy_logo.png', width=150)
st.sidebar.success('BACKEND DEVELOPER')

api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")
if api_key:
    st.session_state.api_key = api_key

bot_type = st.sidebar.radio("Choose a BOT type", 
                            ["Homepage", "Django BOT", "ExpressJS BOT", "Streamlit BOT", "Flask BOT", 
                             "Laravel BOT", "Ruby on Rails BOT", "Spring BOT", "Go BOT", "ASP.NET BOT", "CakePHP BOT", "Clear Conversation"])

if bot_type == "Homepage":
    homepage()
elif bot_type == "Django BOT":
    framework_page("Django", os.path.join(os.getcwd(), "libro-django.pdf"))
elif bot_type == "ExpressJS BOT":
    framework_page("ExpressJS", os.path.join(os.getcwd(), "express-book.pdf"))
elif bot_type == "Streamlit BOT":
    framework_page("Streamlit", os.path.join(os.getcwd(), "Streamlit_book.pdf"))
elif bot_type == "Flask BOT":
    framework_page("Flask", os.path.join(os.getcwd(), "Flask_book.pdf"))
elif bot_type == "Laravel BOT":
    framework_page("Laravel", os.path.join(os.getcwd(), "Laravel_book.pdf"))
elif bot_type == "Ruby on Rails BOT":
    framework_page("Ruby on Rails", os.path.join(os.getcwd(), "Ruby_on_rails_book.pdf"))
elif bot_type == "Spring BOT":
    framework_page("Spring", os.path.join(os.getcwd(), "Spring_book.pdf"))
elif bot_type == "Go BOT":
    framework_page("Go", os.path.join(os.getcwd(), "Go_book.pdf"))
elif bot_type == "ASP.NET BOT":
    framework_page("ASP.NET", os.path.join(os.getcwd(), "ASP.net_BOOK.pdf"))
elif bot_type == "CakePHP BOT":
    framework_page("CakePHP", os.path.join(os.getcwd(), "CakePHPCookBook.pdf"))
elif bot_type == "Clear Conversation":
    clear_conversation_page()
