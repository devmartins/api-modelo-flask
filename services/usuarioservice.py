
from models.usuario import Usuario
from models import db
from dto.respostadto import RespostaDto
from http import HTTPStatus

def listar():
    return [usuario.to_dict() for usuario in Usuario.query.order_by('id').all()], HTTPStatus.OK.value

def obter(id):
    usuario = Usuario.query.get(id)
    if usuario is not None:
        return usuario.to_dict(), HTTPStatus.OK.value

    return {}, HTTPStatus.NOT_FOUND.value

def inserir(dic_usuario):
    usuario = Usuario()
    usuario.nome = dic_usuario.get("nome")

    if usuario.nome is None or usuario.nome == '' or usuario.nome.isspace():
        return RespostaDto("O nome do usuário é inválido").to_dict(), HTTPStatus.BAD_REQUEST.value

    db.session.add(usuario)
    db.session.commit()
    return usuario.to_dict(), HTTPStatus.CREATED.value

def atualizar(id, dic_usuario):
    usuario = Usuario.query.get(id)

    if usuario is not None:
        usuario.nome = dic_usuario.get("nome")

        if usuario.nome is None or usuario.nome == '' or usuario.nome.isspace():
            return RespostaDto("O nome do usuário é inválido").to_dict(), HTTPStatus.BAD_REQUEST.value

        db.session.commit()

        return usuario.to_dict(), HTTPStatus.OK.value

    return RespostaDto("Usuário não encontrado").to_dict(), HTTPStatus.BAD_REQUEST.value

def excluir(id):
    usuario = Usuario.query.get(id)

    if usuario is not None:
        db.session.delete(usuario)
        db.session.commit()

        return {}, HTTPStatus.NO_CONTENT.value

    return {}, HTTPStatus.NOT_FOUND.value
