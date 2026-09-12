from fastapi import FastAPI
from dotenv import load_dotenv
import os
from groq import Groq
from model import ChatRequest , ChatResponse

load_dotenv()

app=FastAPI()

@app.post("/chat", response_model=ChatResponse)
async def chat_with_groq(request: ChatRequest): 
    client = Groq(
        api_key=os.environ.get("groq_api_key"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": request.chats,
            },
            {
                 "role": "system",
                 "content": request.system_prompt,
            }
        ],
        model="openai/gpt-oss-120b",
    )
    return  {
       "response": chat_completion.choices[0].message.content
    }