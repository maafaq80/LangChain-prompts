from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from dotenv import load_dotenv
import os 
load_dotenv()

api_key=os.getenv("OPEN_AI_API_KEY")
model=ChatOpenAI(model="gpt-4o-mini",
                 openai_api_key=api_key)

chat_history=[
    SystemMessage(content="You are a helpful assistant"),
]
while True:
    user_input=input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input=='exit':
        break
    
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)
    
print(chat_history)
