
import requests
from http import HTTPStatus
from testes.config import URL_API

URL_USUARIOS = f"{URL_API}/usuarios"


def test_listagem_usuarios_deve_retornar_status_ok():
    resposta = requests.get(URL_USUARIOS)
    assert resposta.status_code == HTTPStatus.OK.value


def test_inserir_usuario_deve_retornar_status_criado():
    usuario = {"nome": "Moisés"}

    resposta = requests.post(URL_USUARIOS, json=usuario)
    assert resposta.status_code == HTTPStatus.CREATED.value
    return resposta.json()


def test_inserir_usuario_invalido_deve_retornar_status_bad_request():
    usuario = {"nome": None}

    resposta = requests.post(URL_USUARIOS, json=usuario)
    assert resposta.status_code == HTTPStatus.BAD_REQUEST.value


def test_obter_usuario_valido_deve_retornar_ok():
    usuario = test_inserir_usuario_deve_retornar_status_criado()

    resposta = requests.get(f"{URL_USUARIOS}/{usuario['id']}")
    assert resposta.status_code == HTTPStatus.OK.value


def test_obter_usuario_invalido_deve_retornar_nao_encontrado():
    resposta = requests.get(f"{URL_USUARIOS}/0")
    assert resposta.status_code == HTTPStatus.NOT_FOUND.value


def test_atualizar_usuario_deve_retornar_status_ok():
    usuario = test_inserir_usuario_deve_retornar_status_criado()
    usuario["nome"] = "Moisés Atualizado"

    resposta = requests.put(f"{URL_USUARIOS}/{usuario['id']}", json=usuario)
    assert resposta.status_code == HTTPStatus.OK.value


def test_atualizar_usuario_invalido_deve_retornar_status_bad_request():
    usuario = test_inserir_usuario_deve_retornar_status_criado()
    usuario["nome"] = None

    resposta = requests.put(f"{URL_USUARIOS}/{usuario['id']}", json=usuario)
    assert resposta.status_code == HTTPStatus.BAD_REQUEST.value


def test_excluir_usuario_deve_retornar_status_sem_conteudo():
    usuario = test_inserir_usuario_deve_retornar_status_criado()

    resposta = requests.delete(f"{URL_USUARIOS}/{usuario['id']}")
    assert resposta.status_code == HTTPStatus.NO_CONTENT.value


def test_excluir_usuario_inexistente_deve_retornar_status_nao_encontrado():
    resposta = requests.delete(f"{URL_USUARIOS}/0")
    assert resposta.status_code == HTTPStatus.NOT_FOUND.value