
from models import db


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))

    def to_dict(self):
        return {"id": self.id, "nome": self.nome}
