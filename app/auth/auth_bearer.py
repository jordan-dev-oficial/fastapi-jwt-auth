# Autor: jordan dev
# GitHub: jordan-dev
# Este arquivo é responsável por verificar se a requisição está autorizada (proteção de rotas)

from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .auth_handler import decodeJWT

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credenciais: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credenciais:
            if not credenciais.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Esquema de autenticação inválido.")
            
            if not self.verificar_jwt(credenciais.credentials):
                raise HTTPException(status_code=403, detail="Token inválido ou expirado.")
            
            return credenciais.credentials
        else:
            raise HTTPException(status_code=403, detail="Código de autorização inválido.")

    def verificar_jwt(self, jwtoken: str) -> bool:
        token_valido: bool = False

        try:
            payload = decodeJWT(jwtoken)
        except:
            payload = None
        
        if payload:
            token_valido = True
            
        return token_valido