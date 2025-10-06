from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()
model=ChatOpenAI()

chat_template=ChatPromptTemplate.from_messages([
    ('system','you are a helpfull {domain} expert'), # we use this from dynamic prompts 
    ('human', 'Explain in simple terms, what is {topic}')# prompt template is used for single task query 
    # chatprompt template is used for multi task conversation
])
prompts=chat_template.format_messages(
    domain='cricket',
    topic='dusra'
)
print(prompts)