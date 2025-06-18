from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os 

load_dotenv()
api_key=os.getenv("OPEN_AI_API_KEY")
model=ChatOpenAI(model="gpt-4o-mini",
                 openai_api_key=api_key)

messages=[
    SystemMessage(content="You are a helpfull assistant"),
    HumanMessage(content="tell me about langchain in 10 words")
]

result=model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)
