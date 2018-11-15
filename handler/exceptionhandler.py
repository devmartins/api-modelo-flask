
from flask import jsonify
import traceback
from http import HTTPStatus

def erro(exception):
    #print(traceback.format_exc()) #para logar a exceção
    return "{}", HTTPStatus.INTERNAL_SERVER_ERROR