from fastapi import FastAPI
from openai import OpenAI
import os

app = FastAPI()

# Inicializa o cliente apontando para a Base URL (exemplo usando OpenRouter ou Groq)
# Você vai configurar a chave depois nas variáveis de ambiente do Render
client = OpenAI(
    base_url=os.getenv("OPENAI_BASE_URL", "https://api.groq.com/openai/v1"),
    api_key=os.getenv("OPENAI_API_KEY", "sua-chave-aqui")
)

@app.get("/")
def home():
    return {"status": "Pascal online e operacional!"}

@app.get("/perguntar")
def perguntar(prompt: str):
    response = client.chat.completions.create(
        model=os.getenv("DEFAULT_MODEL", "llama-3.3-70b-versatile"),
        messages=[
            {"role": "system", "content": "Você é o Pascal, um assistente pessoal inteligente."},
            {"role": "user", "content": prompt}
        ]
    )
    return {"resposta": response.choices[0].message.content}