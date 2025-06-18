from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os 
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()
api_key=os.getenv("OPEN_AI_API_KEY")

model=ChatOpenAI(model="gpt-4o-mini",
                 openai_api_key=api_key )

st.header("Research Tool")

paper_input=st.text_input("Enter Paper name to summarize")
style_input=st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])
length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )
 
template=load_prompt('template.json')

# prompt=template.invoke({
#     'paper_input':paper_input,
#     'style_input':style_input,
#     'length_input':length_input
# })

if st.button("Summarize"):
    chain=template | model
    result=chain.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
})
    st.write(result.content)