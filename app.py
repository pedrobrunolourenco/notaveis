from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, render_template
from urllib.parse import unquote

from schemas.error import ErrorSchema
from schemas.notavel import ListagemNotaveisSchema, NotavelAddSchema, NotavelUpdSchema, RetornoNotavelSchema, apresenta_notaveis, apresenta_notavel
from sqlalchemy.exc import IntegrityError

from model import Session
from logger import logger
from flask_cors import CORS

from sqlalchemy.orm import aliased


#######################################
from pydantic import BaseModel
from typing import Optional, List
from model.notavel import Notavel
from sqlalchemy import AliasedReturnsRows, delete, func, update;



info = Info(title="API para criação de um notável - Sprint-03", version="1.0.0")
app = OpenAPI(__name__, info=info)

CORS(app)

home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
notavel_tag = Tag(name="Notavel", description="Adição, Edição, visualização e remoção de NOTÁVEIS à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

    
@app.post('/create', tags=[notavel_tag],
          responses={"200": RetornoNotavelSchema, "409": ErrorSchema, "400": ErrorSchema })
def add_notavel(form: NotavelAddSchema):
    """Adiciona um novo notavel à base de dados
    """

    notavel = Notavel(
        nome = form.nome,
        apelido = form.apelido,
        atividade = form.atividade,
        descricao = form.descricao
    )

    logger.debug(f"Adicionando um notável à base: '{notavel.nome}'")
    try:
        session = Session()
        session.add(notavel)
        session.commit()
        return apresenta_notavel(notavel), 200
    except Exception as e:
        error_msg = "Não foi possível salvar o novo notável :/"
        logger.warning(f"Erro ao adicionar um notável '{notavel.nome}', {error_msg}, erro: {e}")
        return {"message": error_msg}, 400

@app.get('/getall', tags=[notavel_tag],
          responses={"200": ListagemNotaveisSchema, "409": ErrorSchema, "400": ErrorSchema})
def get_notaveis():
    """Obtém uma lista de notaveis

    Retorna uma lista de representação dos notaveis
    """
    try:
        session = Session()    
        notaveis = session.query(Notavel).all()
        return apresenta_notaveis(notaveis), 200
    except Exception as e:
        error_msg = "Não foi possível obter listagem de notaveis :/"
        logger.warning(f"Erro ao listar notaveis {error_msg}, erro: {e}")
        return {"message": error_msg}, 400
    

@app.put('/update', tags=[notavel_tag],
          responses={"200": RetornoNotavelSchema, "409": ErrorSchema, "400": ErrorSchema })
def update_notavel(form: NotavelUpdSchema):
    """Altera o dados notavel à base de dados
    """
    logger.debug(f"alterando um notável '{form.nome}'")
    try:
        session = Session()
        stmt = update(Notavel).where(Notavel.id == form.id).values(nome=form.nome, apelido=form.apelido, atividade=form.atividade, descricao=form.descricao)
        session.execute(stmt)
        session.commit() 
        return apresenta_notavel(form), 200
    except Exception as e:
        error_msg = "Não foi possível alterar o notável :/"
        logger.warning(f"Erro ao alterar um notável '{form.nome}', {error_msg}, erro: {e}")
        return {"message": error_msg}, 400

    

