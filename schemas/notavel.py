from pydantic import BaseModel, Field
from typing import List
from model.notavel import Notavel

class NotavelAddSchema(BaseModel):
    """ Define como um novo notavel
    """
    nome: str 
    apelido: str
    atividade: str
    descricao: str

class NotavelUpdSchema(BaseModel):
    """ Define como um novo notavel
    """
    id: int = Field(..., description="Id do Notavel")
    nome: str = Field(..., description="Nome do Notável")
    apelido: str = Field(..., description="Apelido do Notavel")
    atividade: str= Field(..., description="Atividade do Notavel")
    descricao: str = Field(..., description="Resumo")

class RetornoNotavelSchema(BaseModel):
    """ Retorno de um novo notavel
    """
    id: int
    nome: str 
    apelido: str
    atividade: str
    descricao: str

class ListagemNotaveisSchema(BaseModel):
    """ Define como uma listagem de Notaveis será apresentada
    """
    notaveis:List[RetornoNotavelSchema]

class NotaveisGetAllSchema(BaseModel):
    """ faz busca paginada
    """
    offset: str
    limit: str


def apresenta_notavel(notavel: Notavel):
    """ Retorna uma representação de um notável 
    """
    return {
        "id": notavel.id,
        "nome": notavel.nome,
        "apelido": notavel.apelido,
        "atividade": notavel.atividade,
        "descricao": notavel.descricao
    }


def apresenta_notaveis(notaveis: List[Notavel]):
    """ Retorna uma representação de uma lista de notaveis
    """
    result = []
    for notavel in notaveis:
        result.append({
            "id": notavel.id,
            "nome": notavel.nome,
            "apelido": notavel.apelido,
            "atividade": notavel.atividade,
            "descricao": notavel.descricao
        })

    return {"notaveis": result}

