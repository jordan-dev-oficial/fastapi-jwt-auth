from pydantic import BaseModel, Field, EmailStr

# Esquema para criação de novos acessos ao sistema (Registro)
class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Operator Admin",
                "email": "admin@cybernet.com.br",
                "password": "strong_password_hash"
            }
        }

# Esquema para autenticação (Login) no Gateway
class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "admin@cybernet.com.br",
                "password": "strong_password_hash"
            }
        }

# Esquema para os Posts (Conteúdo do sistema)
class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(...)
    content: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "Protocolo de Segurança",
                "content": "Acesso autorizado ao mainframe Cyber-Net."
            }
        }

# Autor: jordan dev