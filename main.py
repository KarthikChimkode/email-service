from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
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

def send_actual_email(to, subject, body, cc):

    msg = MIMEText(body)
    
    msg["Subject"]=subject
    msg["From"]=EMAIL
    msg["To"]=to
    msg["Cc"]=cc 

    with smtplib.SMTP("smtp.gmail.com", 587) as server:

        server.starttls()

        server.login(EMAIL, PASSWORD)

        server.send_message(msg)


@app.post("/send_email")
def send_email(data: EmailRequest):

    send_actual_email(
        data.to,
        data.sub,
        data.body,
        data.cc
    )

    return {"recieved": "Email sent"}