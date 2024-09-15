from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from typing import Union

from  model import Base

class Notavel(Base):
    __tablename__ = 'notavel'

    id = Column("pk_notavel", Integer, primary_key=True)
    nome = Column(String(80))
    apelido = Column(String(30))
    atividade = Column(String(80))
    descricao = Column(String(150))
    imagem =  Column(String(250))

    def __init__(self, nome:str, apelido:str, atividade:str, descricao:str, imagem:str):
        self.nome = nome
        self.apelido = apelido
        self.atividade = atividade
        self.descricao = descricao
        self.imagem = imagem




