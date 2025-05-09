from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from functions.criarTexto import gerar_nome_relatorio, salvar_texto_no_arquivo

app = FastAPI()

class RelatorioRequest(BaseModel):
    texto: str

@app.post("/criar")
async def criar_relatorio(request: RelatorioRequest):
    try:
        # Gera o caminho base (sem extensão) para salvar o relatório
        nome_relatorio = gerar_nome_relatorio(request.texto)
        
        # Salva o texto original no arquivo gerado
        salvar_texto_no_arquivo(request.texto, nome_relatorio)
        
        return {
            "status": "ok",
            "mensagem": "Relatório criado com sucesso!",
            "nome_relatorio": nome_relatorio
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
