import streamlit as st
col1, col2 = st.columns([1, 6])

with col1:    
    st.image('Botarmy_logo.png', width=100)
with col2:
    st.title('BOTARMY-HUB: Become a virtual assistant reseller')

st.info ("Becoming a BOTARMY virtual assistant chatbot reseller is a straightforward process designed to empower individuals and businesses to offer cutting-edge AI-driven solutions to their clients. As a reseller, you gain access to our suite of advanced chatbot technologies, comprehensive training programs, and dedicated support resources. Simply reach out to our team to express your interest in becoming a reseller, and we'll guide you through the onboarding process. Once onboarded, you'll receive all the necessary tools and resources to start reselling BOTARMY chatbots to your clients. With our flexible reseller program, you have the freedom to set your own pricing and customize solutions to meet the unique needs of your clients. Join us in revolutionizing the chatbot industry and unlock new opportunities for growth and success as a BOTARMY virtual assistant chatbot reseller.")
st.warning("But that's not all! When you join our network of Bot Resellers, you'll benefit from:")
list1= ["Comprehensive Training and Support: Receive extensive training and ongoing support from our team of experts to help you master our chatbot technology and grow your business with confidence.", "Lucrative Revenue Opportunities: Tap into a lucrative market and unlock unlimited earning potential as you help businesses harness the power of chatbots to drive results and achieve their goals.", "Cutting-Edge Technology: Stay ahead of the curve with access to the latest advancements in chatbot technology, ensuring that you always offer your clients best-in-class solutions that deliver real value.", "Marketing and Sales Resources: Access a wealth of marketing and sales resources, including marketing collateral, sales materials, and lead generation support, to help you attract and retain clients effectively."]
for item in list1:
        st.info(item)

st.warning("If you want to be a reseller contact wih us with the link below")
st.markdown('<a href="https://wa.me/+5930993513082">I want to be a reseller</a>', unsafe_allow_html=True)
    