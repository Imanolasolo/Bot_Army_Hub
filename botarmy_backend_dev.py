import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI 
from htmlTemplates import css, bot_template, user_template
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
        st.warning("Please upload the textual PDF file - this is PDF files of image")
        return None
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vector_store):
    llm = ChatOpenAI(openai_api_key=st.secrets["OPEN_AI_APIKEY"])
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory
    )
    return conversation_chain

def handle_userInput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

     # Limpiar los mensajes anteriores antes de mostrar los nuevos mensajes
    st.session_state.django_chat_history = []
    st.session_state.expressjs_chat_history = []

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

# Página de inicio
def homepage():
    st.title("Welcome to BOT ARMY")
    st.markdown("BOT ARMY is a platform for creating Backend projects in various frameworks using LLMs (Large Language Models from PDFs and URLs) as engine.")
    st.markdown("With BOT ARMY, you can easily generate code snippets, project structures, and even interact with ChatGPT to get assistance in your development process.")
    st.markdown("Follow these steps to get started:")
    st.success("1. Choose the type of BOT you want to generate.")
    st.warning("2. Train the agent choosing the selector each time you start the bot")
    st.success("3. Start creating your Backend project!")
    st.success("4. After using the bot push 'Clear Conversation' on sidebar to clear the messages and work clearly")
    

def django_page():
    st.title("DjangoBOT Page")
    st.warning("This is the page for Django BOT.")
          
    use_sample_pdf = st.checkbox("Talk with Django Bot")
    if use_sample_pdf:
            sample_pdf_path = os.path.join(os.getcwd(), "libro-django.pdf")
            st.session_state.pdf_files = [sample_pdf_path]
    

        #st.session_state.api_key = st.text_input("Enter your OpenAI API key:")
    train = st.button("Train the Agent")
    if train:
            with st.spinner("Processing"):
                # get the text from PDFs
                raw_text = get_pdf_text(st.session_state.pdf_files)
                st.session_state.pdf_text = raw_text
                # get the text chunks
                text_chunks = get_text_chunks(raw_text)
                # create vector store
                vector_store = get_vector_store(text_chunks)
                # conversation chain
                st.session_state.conversation = get_conversation_chain(vector_store)
                # set train to True to indicate agent has been trained
                st.session_state.train = True
    

    if not st.session_state.train:
        st.warning("First Train the Agent")

    if st.session_state.train:
        st.write("<h5><br>Ask anything from your documents, doesn´t matter the language I am multi-idiomatic !:</h5>", unsafe_allow_html=True)
        user_question = st.text_input(label="", placeholder="Enter something...")
        if user_question:
            handle_userInput(user_question)  

def expressjs_page():
    st.title("Express Page")
    st.warning("This is the page for Express BOT.")
          
    use_sample_pdf = st.checkbox("Talk with Express Bot")
    if use_sample_pdf:
            sample_pdf_path = os.path.join(os.getcwd(), "express-book.pdf")
            st.session_state.pdf_files = [sample_pdf_path]
    

        #st.session_state.api_key = st.text_input("Enter your OpenAI API key:")
    train = st.button("Train the Agent")
    if train:
            with st.spinner("Processing"):
                # get the text from PDFs
                raw_text = get_pdf_text(st.session_state.pdf_files)
                st.session_state.pdf_text = raw_text
                # get the text chunks
                text_chunks = get_text_chunks(raw_text)
                # create vector store
                vector_store = get_vector_store(text_chunks)
                # conversation chain
                st.session_state.conversation = get_conversation_chain(vector_store)
                # set train to True to indicate agent has been trained
                st.session_state.train = True
    

    if not st.session_state.train:
        st.warning("First Train the Agent")

    if st.session_state.train:
        st.write("<h5><br>Ask anything from your documents, doesn´t matter the language I am multi-idiomatic !:</h5>", unsafe_allow_html=True)
        user_question = st.text_input(label="", placeholder="Enter something...")
        if user_question:
            handle_userInput(user_question)

def flask_page():
    st.title("Flask BOT Page")
    st.warning("This is the page for Flask BOT.")
          
    use_sample_pdf = st.checkbox("Talk with Flask Bot")
    if use_sample_pdf:
            sample_pdf_path = os.path.join(os.getcwd(), "Flask_book.pdf")
            st.session_state.pdf_files = [sample_pdf_path]
    

        #st.session_state.api_key = st.text_input("Enter your OpenAI API key:")
    train = st.button("Train the Agent")
    if train:
            with st.spinner("Processing"):
                # get the text from PDFs
                raw_text = get_pdf_text(st.session_state.pdf_files)
                st.session_state.pdf_text = raw_text
                # get the text chunks
                text_chunks = get_text_chunks(raw_text)
                # create vector store
                vector_store = get_vector_store(text_chunks)
                # conversation chain
                st.session_state.conversation = get_conversation_chain(vector_store)
                # set train to True to indicate agent has been trained
                st.session_state.train = True
    

    if not st.session_state.train:
        st.warning("First Train the Agent")

    if st.session_state.train:
        st.write("<h5><br>Ask anything from your documents, doesn´t matter the language I am multi-idiomatic !:</h5>", unsafe_allow_html=True)
        user_question = st.text_input(label="", placeholder="Enter something...")
        if user_question:
            handle_userInput(user_question)

def laravel_page():
    st.title("Laravel BOT Page")
    st.warning("This is the page for Laravel BOT.")
          
    use_sample_pdf = st.checkbox("Talk with Laravel Bot")
    if use_sample_pdf:
            sample_pdf_path = os.path.join(os.getcwd(), "Laravel_book.pdf")
            st.session_state.pdf_files = [sample_pdf_path]
    

        #st.session_state.api_key = st.text_input("Enter your OpenAI API key:")
    train = st.button("Train the Agent")
    if train:
            with st.spinner("Processing"):
                # get the text from PDFs
                raw_text = get_pdf_text(st.session_state.pdf_files)
                st.session_state.pdf_text = raw_text
                # get the text chunks
                text_chunks = get_text_chunks(raw_text)
                # create vector store
                vector_store = get_vector_store(text_chunks)
                # conversation chain
                st.session_state.conversation = get_conversation_chain(vector_store)
                # set train to True to indicate agent has been trained
                st.session_state.train = True
    

    if not st.session_state.train:
        st.warning("First Train the Agent")

    if st.session_state.train:
        st.write("<h5><br>Ask anything from your documents, doesn´t matter the language I am multi-idiomatic !:</h5>", unsafe_allow_html=True)
        user_question = st.text_input(label="", placeholder="Enter something...")
        if user_question:
            handle_userInput(user_question)

def ruby_on_rails_page():
    st.title("Ruby on Rails BOT Page")
    st.warning("This is the page for Ruby on Rails BOT.")
          
    use_sample_pdf = st.checkbox("Talk with Ruby on Rails Bot")
    if use_sample_pdf:
            sample_pdf_path = os.path.join(os.getcwd(), "Ruby_on_rails_book.pdf")
            st.session_state.pdf_files = [sample_pdf_path]
    

        #st.session_state.api_key = st.text_input("Enter your OpenAI API key:")
    train = st.button("Train the Agent")
    if train:
            with st.spinner("Processing"):
                # get the text from PDFs
                raw_text = get_pdf_text(st.session_state.pdf_files)
                st.session_state.pdf_text = raw_text
                # get the text chunks
                text_chunks = get_text_chunks(raw_text)
                # create vector store
                vector_store = get_vector_store(text_chunks)
                # conversation chain
                st.session_state.conversation = get_conversation_chain(vector_store)
                # set train to True to indicate agent has been trained
                st.session_state.train = True
    

    if not st.session_state.train:
        st.warning("First Train the Agent")

    if st.session_state.train:
        st.write("<h5><br>Ask anything from your documents, doesn´t matter the language I am multi-idiomatic !:</h5>", unsafe_allow_html=True)
        user_question = st.text_input(label="", placeholder="Enter something...")
        if user_question:
            handle_userInput(user_question)

def spring_page():
    st.title("Spring BOT Page")
    st.warning("This is the page for Spring BOT.")
          
    use_sample_pdf = st.checkbox("Talk with Spring Bot")
    if use_sample_pdf:
            sample_pdf_path = os.path.join(os.getcwd(), "Spring_book.pdf")
            st.session_state.pdf_files = [sample_pdf_path]
    

        #st.session_state.api_key = st.text_input("Enter your OpenAI API key:")
    train = st.button("Train the Agent")
    if train:
            with st.spinner("Processing"):
                # get the text from PDFs
                raw_text = get_pdf_text(st.session_state.pdf_files)
                st.session_state.pdf_text = raw_text
                # get the text chunks
                text_chunks = get_text_chunks(raw_text)
                # create vector store
                vector_store = get_vector_store(text_chunks)
                # conversation chain
                st.session_state.conversation = get_conversation_chain(vector_store)
                # set train to True to indicate agent has been trained
                st.session_state.train = True
    

    if not st.session_state.train:
        st.warning("First Train the Agent")

    if st.session_state.train:
        st.write("<h5><br>Ask anything from your documents, doesn´t matter the language I am multi-idiomatic !:</h5>", unsafe_allow_html=True)
        user_question = st.text_input(label="", placeholder="Enter something...")
        if user_question:
            handle_userInput(user_question)

def go_page():
    st.title("Go BOT Page")
    st.warning("This is the page for Go BOT.")

    use_sample_pdf = st.checkbox("Talk with Go Bot")
    if use_sample_pdf:
            sample_pdf_path = os.path.join(os.getcwd(), "Go_book.pdf")
            st.session_state.pdf_files = [sample_pdf_path]
    

        #st.session_state.api_key = st.text_input("Enter your OpenAI API key:")
    train = st.button("Train the Agent")
    if train:
            with st.spinner("Processing"):
                # get the text from PDFs
                raw_text = get_pdf_text(st.session_state.pdf_files)
                st.session_state.pdf_text = raw_text
                # get the text chunks
                text_chunks = get_text_chunks(raw_text)
                # create vector store
                vector_store = get_vector_store(text_chunks)
                # conversation chain
                st.session_state.conversation = get_conversation_chain(vector_store)
                # set train to True to indicate agent has been trained
                st.session_state.train = True
    

    if not st.session_state.train:
        st.warning("First Train the Agent")

    if st.session_state.train:
        st.write("<h5><br>Ask anything from your documents, doesn´t matter the language I am multi-idiomatic !:</h5>", unsafe_allow_html=True)
        user_question = st.text_input(label="", placeholder="Enter something...")
        if user_question:
            handle_userInput(user_question)

def asp_net_page():
    st.title("Spring ASP.NET Page")
    st.warning("This is the page for ASP.NET BOT.")
          
    use_sample_pdf = st.checkbox("Talk with ASP.NET Bot")
    if use_sample_pdf:
            sample_pdf_path = os.path.join(os.getcwd(), "ASP.net_BOOK.pdf")
            st.session_state.pdf_files = [sample_pdf_path]
    

        #st.session_state.api_key = st.text_input("Enter your OpenAI API key:")
    train = st.button("Train the Agent")
    if train:
            with st.spinner("Processing"):
                # get the text from PDFs
                raw_text = get_pdf_text(st.session_state.pdf_files)
                st.session_state.pdf_text = raw_text
                # get the text chunks
                text_chunks = get_text_chunks(raw_text)
                # create vector store
                vector_store = get_vector_store(text_chunks)
                # conversation chain
                st.session_state.conversation = get_conversation_chain(vector_store)
                # set train to True to indicate agent has been trained
                st.session_state.train = True
    

    if not st.session_state.train:
        st.warning("First Train the Agent")

    if st.session_state.train:
        st.write("<h5><br>Ask anything from your documents, doesn´t matter the language I am multi-idiomatic !:</h5>", unsafe_allow_html=True)
        user_question = st.text_input(label="", placeholder="Enter something...")
        if user_question:
            handle_userInput(user_question)

def cake_php_page():
    st.title("CakePHP Page")
    st.warning("This is the page for CakePHP BOT.")
          
    use_sample_pdf = st.checkbox("Talk with CakePHP Bot")
    if use_sample_pdf:
            sample_pdf_path = os.path.join(os.getcwd(), "CakePHPCookBook.pdf")
            st.session_state.pdf_files = [sample_pdf_path]
    

        #st.session_state.api_key = st.text_input("Enter your OpenAI API key:")
    train = st.button("Train the Agent")
    if train:
            with st.spinner("Processing"):
                # get the text from PDFs
                raw_text = get_pdf_text(st.session_state.pdf_files)
                st.session_state.pdf_text = raw_text
                # get the text chunks
                text_chunks = get_text_chunks(raw_text)
                # create vector store
                vector_store = get_vector_store(text_chunks)
                # conversation chain
                st.session_state.conversation = get_conversation_chain(vector_store)
                # set train to True to indicate agent has been trained
                st.session_state.train = True
    

    if not st.session_state.train:
        st.warning("First Train the Agent")

    if st.session_state.train:
        st.write("<h5><br>Ask anything from your documents, doesn´t matter the language I am multi-idiomatic !:</h5>", unsafe_allow_html=True)
        user_question = st.text_input(label="", placeholder="Enter something...")
        if user_question:
            handle_userInput(user_question)

def clear_conversation_page():
    st.title("CakePHP BOT Page")
    st.info("Check a bot from sidebar")

# Sidebar actions
st.sidebar.image('Botarmy_logo.png', width=150)
st. sidebar.success('BACKEND DEVELOPER')


bot_type = st.sidebar.radio("Choose a BOT type", 
                             ["Django BOT", "ExpressJS BOT", "Flask BOT", 
                              "Laravel BOT", "Ruby on Rails BOT", 
                              "Spring BOT", "ASP.NET BOT", 
                              "Go BOT", "CakePHP BOT","Clear Conversation"])

if bot_type == "Clear Conversation":
    st.write('<style> .css-12l95y4 { background-color: #FF5733; color: white; } </style>', unsafe_allow_html=True)
 # Add a text input widget in the sidebar to allow users to input the API key globally
api_key = st.sidebar.text_input("Enter your OpenAI API key:")   
# Mostrar la página de inicio
homepage()

# Determinar qué página mostrar según la selección del usuario
if bot_type == "Django BOT":
    django_page()
elif bot_type == "ExpressJS BOT":
    expressjs_page()
elif bot_type == "Flask BOT":
    flask_page()
elif bot_type == "Laravel BOT":
    laravel_page()
elif bot_type == "Ruby on Rails BOT":
    ruby_on_rails_page()
elif bot_type == "Spring BOT":
    spring_page()
elif bot_type == "ASP.NET BOT":
    asp_net_page()
elif bot_type == "Go BOT":
    go_page()
elif bot_type == "CakePHP BOT":
    cake_php_page()
elif bot_type == "Clear conversation":
    clear_conversation_page()


# Main screen actions

