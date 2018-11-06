
from flask import jsonify, Blueprint, request
from services import usuarioservice
from controllers.basecontroller import to_json


usuarios_bp = Blueprint('usuario', __name__, url_prefix="/usuarios")

@usuarios_bp.route("", methods=["get"])
def listar():
    return to_json(usuarioservice.listar())

@usuarios_bp.route("/<id>", methods=["get"])
def obter(id):
    return to_json(usuarioservice.obter(id))

@usuarios_bp.route("", methods=["post"])
def inserir():
    return to_json(usuarioservice.inserir(request.json))

@usuarios_bp.route("/<id>", methods=["put"])
def atualizar(id):
    return to_json(usuarioservice.atualizar(id, request.json))

@usuarios_bp.route("/<id>", methods=["delete"])
def excluir(id):
    return to_json(usuarioservice.excluir(id))
