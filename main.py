from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class SomRequest(BaseModel):
    nome: str
    descricao: str

@app.post("/gerar-som")
async def gerar_som(data: SomRequest):
    # Simulação de geração de som
    print(f"Gerando som: {data.nome}")
    print(f"Descrição: {data.descricao}")

    # Aqui no futuro: chamar OpenAI API + gerar áudio de verdade
    return {
        "mensagem": "Som gerado com sucesso!",
        "nome": data.nome,
        "descricao": data.descricao
    }
