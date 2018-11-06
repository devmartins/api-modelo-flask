
from flask import jsonify
import traceback
from enums.httpstatus import HttpStatus

def erro(exception):
    #print(traceback.format_exc()) #para logar a exceção
    return "{}", HttpStatus.INTERNAL_SERVER_ERROR