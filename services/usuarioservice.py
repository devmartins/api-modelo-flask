
from models.usuario import Usuario
from models import db
from dto.respostadto import RespostaDto
from enums.httpstatus import HttpStatus

def listar():
    return [usuario.to_dict() for usuario in Usuario.query.order_by('id').all()], HttpStatus.OK

def obter(id):
    usuario = Usuario.query.get(id)
    if usuario is not None:
        return usuario.to_dict(), HttpStatus.OK

    return {}, HttpStatus.NOT_FOUND

def inserir(dic_usuario):
    usuario = Usuario()
    usuario.nome = dic_usuario.get("nome")

    if usuario.nome is None or usuario.nome == '' or usuario.nome.isspace():
        return RespostaDto("O nome do usuário é inválido").to_dict(), HttpStatus.BAD_REQUEST

    db.session.add(usuario)
    db.session.commit()
    return usuario.to_dict(), HttpStatus.CREATED

def atualizar(id, dic_usuario):
    usuario = Usuario.query.get(id)

    if usuario is not None:
        usuario.nome = dic_usuario.get("nome")

        if usuario.nome is None or usuario.nome == '' or usuario.nome.isspace():
            return RespostaDto("O nome do usuário é inválido").to_dict(), HttpStatus.BAD_REQUEST

        db.session.commit()

        return usuario.to_dict(), HttpStatus.OK

    return RespostaDto("Usuário não encontrado").to_dict(), HttpStatus.BAD_REQUEST

def excluir(id):
    usuario = Usuario.query.get(id)

    if usuario is not None:
        db.session.delete(usuario)
        db.session.commit()

        return {}, HttpStatus.NO_CONTENT

    return {}, HttpStatus.NOT_FOUND
