from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGroq(
    model = "openai/gpt-oss-120b",
    temperature = 0.5
)

prompt = ChatPromptTemplate.from_messages([
     (
        "system",
        "You are an {persona} assistant do not answer anything other than {persona} queries."
    ),
    (
        "human",
        "Explain {msg} in simple terms."
    )
])

# prompt = ChatPromptTemplate.from_template(
#     "what is {msg},explain in simple terms in 120 words."
# )

# message = [
#     SystemMessage(
#         content = "u are a medical expert who only has knowledge in medical field u dont know anything else other"
#     ),
#     HumanMessage(
#         content = "what is python in programming language"
#     )
# ]

chain = prompt | llm

response = chain.invoke({
    "msg": "enviroimental factors which affects indian economy",
    "persona" : "medical"
})

print(response.content)