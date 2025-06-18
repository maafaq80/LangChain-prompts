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
length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 lines)", "Medium (3-5 lines)", "Long (detailed explanation)"] )
 


template=PromptTemplate(
    template="""
    Please summarize the research paper titled \"{paper_input}\" with the following specifications:\nExplanation Style: {style_input}  
    Explanation Length: {length_input}  
1. Mathematical Details:  
	- Include relevant mathematical equations if present in the paper.
	- Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
2. Analogies:  
	- Use relatable analogies to simplify complex ideas. 

If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",
input_variable=['paper_input','style_input','length_input'],
validate_template=True
)

prompt=template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
})

if st.button("Summarize"):
    result=model.invoke(prompt)
    st.write(result.content)