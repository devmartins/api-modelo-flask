
from flask import jsonify

to_json = lambda resultado: (jsonify(resultado[0]), resultado[1])
