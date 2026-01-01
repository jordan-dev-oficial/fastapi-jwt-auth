# Autor: jordan dev
# GitHub: jordan-dev
# Responsável por assinar, codificar, decodificar e retornar os tokens JWT

import time
from typing import Dict
import jwt
from decouple import config

# Configurações lidas do arquivo .env
JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

def resposta_token(token: str):
    """Retorna o dicionário com o token de acesso formatado."""
    return {
        "access_token": token
    }

def signJWT(user_id: str) -> Dict[str, str]:
    """Função usada para assinar e gerar a string do JWT."""
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600 # Token expira em 10 minutos
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return resposta_token(token)

def decodeJWT(token: str) -> dict:
    """Função para validar e decodificar o token enviado pelo cliente."""
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        # Verifica se o token ainda está no prazo de validade
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        # Se o token for inválido ou houver erro, retorna um dicionário vazio
        return {}