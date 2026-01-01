# Autor: jordan dev | Codename: Cyber-Shadow
# GitHub: https://github.com/jordan-dev-oficial
# Status: PROTOCOLO DE SEGURANÇA ATIVADO

import uvicorn
from fastapi import FastAPI, Body, Depends, HTTPException
from fastapi.responses import RedirectResponse
from app.model import PostSchema, UserSchema, UserLoginSchema
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT

# Estilização CSS para injetar o tema Hacker no Swagger UI
description = """
<style>
    .swagger-ui .topbar { background-color: #001a00 !important; border-bottom: 2px solid #00ff00; }
    .swagger-ui .info .title { color: #00ff00 !important; font-family: 'Courier New', monospace; text-shadow: 0 0 10px #00ff00; }
    .swagger-ui .scheme-container { background-color: #0d0d0d !important; }
    .renderedMarkdown p, .renderedMarkdown li { color: #00ff00 !important; font-family: 'Courier New', monospace; }
    .swagger-ui .opblock .opblock-summary-description { color: #00ff00 !important; }
</style>

## ⚡ CYBER-NET GATEWAY v2.0 ⚡
**SISTEMA DE ACESSO RESTRITO - MONITORAMENTO JWT ATIVO**

### 🔓 PROTOCOLOS DE INFILTRAÇÃO:
1.  **REGISTRO**: Crie sua identidade digital em [**AUTH > /user/signup**](#/Autentica%C3%A7%C3%A3o/criar_usuario_user_signup_post).
2.  **EXTRAÇÃO**: Obtenha sua chave de acesso em [**AUTH > /user/login**](#/Autentica%C3%A7%C3%A3o/login_usuario_user_login_post).
3.  **BYPASS**: Insira o `access_token` no botão **Authorize** (o cadeado no topo).
4.  **DECODE**: Explore os arquivos protegidos na seção **DATA_FILES**.

---
**Mainframe administrado por: Jordan Dev Oficial**
"""

app = FastAPI(
    title="[ RESTRITO ] - Protocolo Cyber-Auth",
    description=description,
    version="2.0.0-CYBER",
    contact={
        "name": " Jordan Dev Oficial (Cyber-Shadow)",
        "url": "https://github.com/jordan-dev-oficial",
    }
)

# Arquivos Confidenciais (Base de Dados)
postagens = [
    {
        "id": 1,
        "titulo": "OPERACAO_SILENCE",
        "texto": "Logs capturados do servidor central. Vulnerabilidade encontrada no Node-04."
    },
    {
        "id": 2,
        "titulo": "FIREWALL_BYPASS",
        "texto": "Protocolo de injeção de pacotes via porta 10000. Sucesso na infiltração."
    },
    {
        "id": 3,
        "titulo": "ENCRYPT_KEY_X",
        "texto": "Chave de criptografia AES encontrada no diretório oculto da corporação."
    },
]

usuarios = []

def verificar_usuario(dados: UserLoginSchema):
    for usuario in usuarios:
        if usuario.email == dados.email and usuario.password == dados.password:
            return True
    return False

# --- KERNEL ROUTES ---

@app.get("/", include_in_schema=False)
def boot_sequence():
    """Redirecionamento automático para o terminal de comando."""
    return RedirectResponse(url='/docs')

@app.get("/status", tags=["Kernel"])
def system_check():
    """Verifica a integridade do sistema do jordan dev."""
    return {
        "status": "ONLINE",
        "node": "jordan-dev-terminal-01",
        "security_level": "MAXIMUM",
        "encryption": "JWT_HS256"
    }

@app.get("/posts", tags=["Data_Files"])
def obter_arquivos():
    """Lista todos os arquivos descriptografados (Público)."""
    return {"arquivos": postagens}

@app.post("/posts", dependencies=[Depends(JWTBearer())], tags=["Data_Files"])
def injetar_dados(post: PostSchema):
    """Injeta novos dados no sistema (🔒 Requer Chave JWT)."""
    post.id = len(postagens) + 1
    post_data = post.model_dump() if hasattr(post, 'model_dump') else post.dict()
    postagens.append(post_data)
    return {"status": "Upload concluído com sucesso no mainframe!"}

@app.post("/user/signup", tags=["Autenticação"])
def criar_identidade(user: UserSchema = Body(...)):
    """Gera uma nova identidade digital no banco de dados."""
    usuarios.append(user)
    return signJWT(user.email)

@app.post("/user/login", tags=["Autenticação"])
def extrair_token(user: UserLoginSchema = Body(...)):
    """Valida credenciais e extrai o Token de Acesso JWT."""
    if verificar_usuario(user):
        return signJWT(user.email)
    raise HTTPException(status_code=401, detail="ACESSO NEGADO: Credenciais Inválidas.")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)