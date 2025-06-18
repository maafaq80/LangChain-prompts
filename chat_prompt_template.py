from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os 

load_dotenv()
api_key=os.getenv("OPEN_AI_API_KEY")
chat_template=ChatPromptTemplate(
    [('system','You are a helpful {domain} expert'),
    ('human','Explain in simple terms what is {topic}')]
)

prompt=chat_template.invoke({
    'domain':'cricket',
    'topic':'Dusra'
})

model=ChatOpenAI(model="gpt-4o-mini",
                 openai_api_key=api_key)

result=model.invoke(prompt)
print(result.content)

