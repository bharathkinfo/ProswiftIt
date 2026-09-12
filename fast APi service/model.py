from pydantic import BaseModel


class ChatRequest(BaseModel):
    chats : str 
    system_prompt: str = "You are a helpful AI assistant."

class ChatResponse(BaseModel):
    response: str