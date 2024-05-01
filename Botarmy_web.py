import streamlit as st

st.set_page_config(page_title="BOTARMY-HUB", page_icon=":clipboard:")

# Título de la página
col1, col2 = st.columns([1, 6])

with col1:    
    st.image('Botarmy_logo.png', width=100)
with col2:
    st.title('BOTARMY-HUB: Virtual assistants for professionals & companies')

# Subtítulo
st.subheader('Welcome to the future of automation')

# Menú de navegación
menu = ['Home', 'About us', 'Services', 'Contact']
opcion = st.sidebar.selectbox('Navegation', menu)

# Página de inicio
if opcion == 'Home':
    code_message ="""
    Welcome to BOTARMY-HUB, where cutting-edge virtual assistants meet your business needs. 
    We're not just about chatbots; we're transforming how businesses operate in the digital age. 
    Our dedicated team crafts personalized solutions to streamline workflows, boost productivity, 
    and enhance customer experiences. 
    Whether you're a startup or an enterprise, BOTARMY-HUB has the expertise to help you thrive. 
    Join us at the forefront of automation and unlock your business's full potential today."""
    st.success(code_message)

# Página "Sobre Nosotros"
elif opcion == 'About us':
    code_message ="""
    Welcome to BOTARMY-HUB, where innovation drives excellence. Our passionate team of tech enthusiasts pushes the boundaries of virtual assistant technology. We harness the power of AI and automation to empower professionals and businesses worldwide. With a focus on creativity, reliability, and exceptional customer service, we deliver cutting-edge solutions that revolutionize business operations. Our mission: provide clients with the tools to thrive in the digital landscape. Join us on this journey of innovation, and let's build the future together with BOTARMY-HUB."""
    
    st.warning(code_message)

# Página de Servicios
elif opcion == 'Services':
    code_message ="""
    Unlock the potential of BOTARMY-HUB's services to elevate your business. Our experts specialize in tailored solutions across industries, from enhancing customer engagement to streamlining processes. Explore our services:

 - Customized Chatbot Development: Personalized AI-driven chatbots.
 - Integration Services: Seamless integration into existing workflows.
 - Automation Strategy Consulting: Expert guidance for effective strategies.
 - Ongoing Support: Dedicated team ensuring smooth operations.

Transform your business with BOTARMY-HUB today."""
    
    st.info(code_message)

# Página de Contacto
elif opcion == 'Contact':
    code_message = """
    Ready to innovate? Connect with BOTARMY-HUB to explore synergies and unlock new possibilities. Whether you're kickstarting a project or exchanging insights, we're here to collaborate. Drop a message, schedule a call - let's pave the way for innovation!"""

    st.warning(code_message)
    
    col1, col2, col3, col4 =st.columns(4)
    with col1:
        st.image('mail_icon.png', width=80)
        st.markdown('<a href="mailto:jjusturi@gmail.com">Send me a mail</a>', unsafe_allow_html=True)
           
    with col2:
        st.image('whatsapp_logo.png', width=100)
        st.markdown('<a href="https://wa.me/+5930993513082">Send a whatsapp message</a>', unsafe_allow_html=True)

    with col3:
        st.image('meeting_icon.png', width=100)
        st.markdown('<a href="https://buymeacoffee.com/imanolasolo">Let`s have a coffee and have a consultation about technical issues or Coach & Coffee!</a>', unsafe_allow_html=True)
    with col4:
        st.image('linkedin_logo.png', width=80)
        st.markdown('<a href="https://www.linkedin.com/in/imanolasolo/">Find me on Linkedin!</a>', unsafe_allow_html=True)

# Menú de navegación II
menu2 = ['Chat with us', 'Want to be a Bot reseller?']
opcion = st.sidebar.selectbox('Interact with us', menu2)

if opcion == 'Chat with us':
    st.write("You selected to chat with us")
    # Redireccionar al usuario a un enlace específico
    st.markdown("[Go to chat](https://imanol-asolo-ai-chat.streamlit.app/)")

if opcion == 'Want to be a Bot reseller?':
    st.write("You selected to how to resell our bots")
    
    st.success("Are you ready to take your entrepreneurial journey to the next level? Do you have a passion for cutting-edge technology and a drive to succeed in the ever-evolving world of digital innovation? Then look no further, because BOTARMY-HUB is offering you the opportunity of a lifetime!")
    st.info("As a BOTARMY-HUB Bot Reseller, you'll gain access to industry-leading chatbot technology that empowers businesses to enhance their customer experience, streamline their operations, and drive growth like never before. With our customizable chatbot solutions tailored to meet the unique needs of every client, you'll have the power to transform businesses across industries and make a real impact in the digital landscape.")
