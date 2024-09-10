from pydantic import BaseModel
from typing import List
from model.notavel import Notavel

class NotavelAddSchema(BaseModel):
    """ Define como um novo notavel
    """
    nome: str 
    apelido: str
    atividade: str
    descricao: str

class RetornoNotavelSchema(BaseModel):
    """ Retorno de um novo notavel
    """
    id: int
    nome: str 
    apelido: str
    atividade: str
    descricao: str


def apresenta_notavel(notavel: RetornoNotavelSchema):
    """ Retorna uma representação de um notável 
    """
    return {
        "id": notavel.id,
        "nome": notavel.nome,
        "apelido": notavel.apelido,
        "atividade": notavel.atividade,
        "descricao": notavel.descricao
    }

