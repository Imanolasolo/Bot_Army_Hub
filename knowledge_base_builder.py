import streamlit as st
from openai import OpenAI
import PyPDF2
from fpdf import FPDF

# Función para configurar la API de OpenAI con la clave proporcionada
def setup_openai_api(api_key):
    openai.api_key = api_key

def main():
    st.title("Knowledge Base Builder")
    st.info("This application has been created so that from a PDF, Chatgpt 3.5 or an edited text we can create a knowledge base in .pdf or .txt to use in our BOTARMY bots.")

    # Sección para insertar la clave API de OpenAI desde el sidebar
    st.sidebar.header("OpenAI API Configuration")
    st.sidebar.success("Enter your OpenAI API key in the provided text field and press Enter to configure the API.")
    openai_api_key = st.sidebar.text_input("Enter your OpenAI API Key")
    
    # Sección para cargar archivos PDF
    st.header("Upload PDF Files")
    st.warning("1. Drag and drop PDF files into the designated area or click'Upload PDF files'to select files from your device.")
    st.warning("2. The content of the uploaded PDF files will be displayed in the text editing area.")
    uploaded_files = st.file_uploader("Upload PDF files", accept_multiple_files=True)
    
    # Sección para editar el contenido
    st.header("Edit Content")
    st.info("Edit or add additional content to the knowledge base in the provided text area.")
    content = st.text_area("Edit or add content to the knowledge base")

    # Si se carga un archivo PDF, mostrar su contenido en el text_area
    if uploaded_files:
        for pdf_file in uploaded_files:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                content += pdf_reader.pages[page_num].extract_text()
        st.text_area("PDF Content", value=content, height=500)
    
    # Botón para guardar la base de conocimiento en formato PDF
    if st.button("Save as PDF"):
        save_as_pdf(content)

    # Botón para guardar la base de conocimiento en formato de texto plano
    if st.button("Save as Text"):
        save_as_text(content)

    # Mostrar respuesta de ChatGPT debajo del contenido del PDF
    st.header("Chat with GPT-3")
    st.success("1. Exchange messages with OpenAI's GPT-3 model in the chat area. Don´t forget to insert your OpenAI API key in sidebar")
    st.success("2. Enter your message in the input field and click 'Submit' to send it.")
    st.success("3. The response from the GPT-3 model will be displayed in the chat area.")
    st.success("4. Copy & paste it on editor area if you want to save it")
    client = OpenAI(api_key=openai_api_key)

    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})

def save_as_pdf(content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, content)
    with st.spinner("Generating PDF..."):
        st.download_button(
            label="Save PDF",
            data=pdf.output(dest="S").encode("latin1"),
            file_name="knowledge_base.pdf",
            mime="application/pdf"
        )

def save_as_text(content):
    with st.spinner("Saving Text..."):
        st.download_button(
            label="Save Text",
            data=content,
            file_name="knowledge_base.txt",
            mime="text/plain",
            key="download_txt",
            help="Click to download the text file"
        )

# Incluye CSS personalizado para cambiar el color de fondo de los botones
st.markdown(
    """
    <style>
    .stButton>button[data-baseweb="button"] {
        background-color: red !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if __name__ == "__main__":
    main()
