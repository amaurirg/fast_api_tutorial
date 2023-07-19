from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import openai
from decouple import config

app = FastAPI()

origins = [
    "*"
    # "http://localhost",
    # "http://localhost:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

openai.api_key = config("API_KEY")

# Defina a rota para a sua API
@app.get("/chat/{message}")
async def chat(message: str):
    # Envie a mensagem para o modelo ChatGPT
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message,
        # prompt="você é um robô?",
        temperature=0,
        max_tokens=1024
    )
    # Retorne a resposta gerada pelo modelo
    return response.choices[0].text.strip()
