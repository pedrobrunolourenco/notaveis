from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from model.notavel import Notavel
from schemas.error import ErrorSchema
from schemas.notavel import ListagemNotaveisSchema, NotaveisGetPorIdSchema, NotaveisGetPorNomeSchema, NotavelAddSchema, NotavelUpdSchema, NotaveisGetAllSchema, RetornoNotavelSchema, RetornoRemoveSchema, apresenta_notaveis, apresenta_notavel, apresenta_remove
from model import Session
from logger import logger
from flask_cors import CORS
from sqlalchemy import update
from sqlalchemy.orm import aliased

info = Info(title="API para criação de um notável - Sprint-03", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

notavel_tag = Tag(name="Notavel", description="Adição, Edição, visualização e remoção de NOTÁVEIS à base")


@app.get('/')
def home():
    return redirect('/openapi')

@app.post('/create', tags=[notavel_tag],
          responses={"200": RetornoNotavelSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_notavel(form: NotavelAddSchema):
    """Adiciona um novo notavel à base de dados"""
    notavel = Notavel(
        nome=form.nome,
        apelido=form.apelido,
        atividade=form.atividade,
        descricao=form.descricao
    )
    logger.debug(f"Adicionando um notável à base: '{notavel.nome}'")
    try:
        session = Session()
        session.add(notavel)
        session.commit()
        return apresenta_notavel(True, notavel), 200
    except Exception as e:
        error_msg = "Não foi possível salvar o novo notável :/"
        logger.warning(f"Erro ao adicionar um notável '{notavel.nome}', {error_msg}, erro: {e}")
        return {"sucesso": False, "message": error_msg}, 400

@app.get('/getall', tags=[notavel_tag],
          responses={"200": ListagemNotaveisSchema, "409": ErrorSchema, "400": ErrorSchema})
def get_notaveis(query: NotaveisGetAllSchema):
    """Obtém uma lista de notaveis"""
    try:
        limit = query.limit
        offset = query.offset
        session = Session()
        notaveis = session.query(Notavel).limit(limit).offset(offset).all()
        return apresenta_notaveis(True, notaveis), 200
    except Exception as e:
        error_msg = "Não foi possível obter listagem de notaveis :/"
        logger.warning(f"Erro ao listar notaveis {error_msg}, erro: {e}")
        return {"sucesso": False, "message": error_msg}, 400

    
@app.get('/getbyid', tags=[notavel_tag],
          responses={"200": ListagemNotaveisSchema, "409": ErrorSchema, "400": ErrorSchema})
def get_por_id(query: NotaveisGetPorIdSchema):
    """Obtém um notavel por Id"""
    try:
        session = Session()
        notavel = session.query(Notavel).filter(Notavel.id == query.id).first()
        return apresenta_notavel(True, notavel), 200
    except Exception as e:
        error_msg = "Não foi possível obter o notável :/"
        logger.warning(f"Erro ao pesquiar o notável {error_msg}, erro: {e}")
        return {"sucesso": False, "message": error_msg}, 400

    
@app.get('/getbynome', tags=[notavel_tag],
          responses={"200": ListagemNotaveisSchema, "409": ErrorSchema, "400": ErrorSchema})
def get_por_nome(query: NotaveisGetPorNomeSchema):
    """Obtém um notavel por parte do nome"""
    try:
        session = Session()
        notaveis = session.query(Notavel).filter(Notavel.nome.ilike(f"%{query.nome}%"))
        return apresenta_notaveis(True, notaveis), 200
    except Exception as e:
        error_msg = "Não foi possível obter o notável :/"
        logger.warning(f"Erro ao pesquiar o notável {error_msg}, erro: {e}")
        return {"sucesso": False, "message": error_msg}, 400


@app.put('/update', tags=[notavel_tag],
          responses={"200": RetornoNotavelSchema, "409": ErrorSchema, "400": ErrorSchema})
def update_notavel(form: NotavelUpdSchema):
    """Altera o dados notavel à base de dados"""
    logger.debug(f"alterando um notável '{form.nome}'")
    try:
        session = Session()
        stmt = update(Notavel).where(Notavel.id == form.id).values(nome=form.nome, apelido=form.apelido, atividade=form.atividade, descricao=form.descricao)
        result = session.execute(stmt)
        # Verificar se alguma linha foi afetada pela query
        if result.rowcount > 0:
            session.commit()
            return apresenta_notavel(True, form), 200
        else:
            session.rollback()
            return {"sucesso": False, "message": f"O notável com código {form.id} não foi localizado"}, 400
    except Exception as e:
        error_msg = "Não foi possível alterar o notável :/"
        logger.warning(f"Erro ao alterar um notável '{form.nome}', {error_msg}, erro: {e}")
        return {"sucesso": False, "message": error_msg}, 400

@app.delete('/removebyid', tags=[notavel_tag],
          responses={"200": RetornoRemoveSchema, "409": RetornoRemoveSchema, "400": RetornoRemoveSchema})
def remove_po_id(query: NotaveisGetPorIdSchema):
    """Remove um notavel por Id"""
    try:
        session = Session()
        count = session.query(Notavel).filter(Notavel.id == query.id).delete()
        session.commit()
        if count:
           return apresenta_remove(True, f"Notável de código {query.id} excluído com sucesso "), 200
        else:
           return apresenta_remove(False, f"Notável de código {query.id} não encontrado "), 200
            
    except Exception as e:
        error_msg =  f"Notável de código {query.id} => Erro na exclusão {e}"
        logger.warning(f"Erro ao pesquiar o notável {error_msg}, erro: {e}")
        return {"sucesso": False, "message": error_msg}, 400

