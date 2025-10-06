from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI

# chat_template
chat_template=ChatPromptTemplate([
    ('system', 'you are a helpfull customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human' , '{query}')
])

# load chat history
chat_history=[]
with open('chat_history.txt') as f:
    chat_history.extend(f.readline())
print(chat_history)

# create prompt
prompt=chat_template.invoke({
    'chat_history':chat_history,
    'query':'where is my refund'

})
print(prompt)