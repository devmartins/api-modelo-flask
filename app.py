
from flask import Flask
from controllers import *
from models import db
from handler import exceptionhandler
from enums.httpstatus import HttpStatus

app = Flask("Api Modelo")
app.register_blueprint(usuariocontroller.usuarios_bp)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/apimodelos'
db.init_app(app)
app.register_error_handler(HttpStatus.INTERNAL_SERVER_ERROR, exceptionhandler.erro)

if __name__ == "__main__":
    app.run(debug=False)
