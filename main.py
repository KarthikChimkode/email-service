from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"messages": "Mail service running"}

class EmailRequest(BaseModel):
    to: str
    cc: list[str] | None = None
    sub: str 
    body: str

@app.post("/send_email")
def send_email(data: EmailRequest):
    return {"recieved": data}