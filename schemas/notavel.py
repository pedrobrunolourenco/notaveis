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

class NotavelUpdSchema(BaseModel):
    """ Define como um novo notavel
    """
    id: int
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

class ListagemNotaveisSchema(BaseModel):
    """ Define como uma listagem de Notaveis será apresentada
    """
    notaveis:List[RetornoNotavelSchema]



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

