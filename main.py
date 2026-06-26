from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os

app = FastAPI()

load_dotenv()

EMAIL=os.getenv("EMAIL")
PASSWORD=os.getenv("PASSWORD")
    

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