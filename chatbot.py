from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.6-flash')

chat_history =[]

while (True):
    user_input = input("you :")
    if user_input == 'exit':
        break
    chat_history.append(user_input)
    result=model.invoke(chat_history)
    chat_history.append(dict(result.content[0])['text'])
    print('AI: ',dict(result.content[0])['text'])