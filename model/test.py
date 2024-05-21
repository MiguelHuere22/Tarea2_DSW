from utils.db import db
from dataclasses import dataclass

@dataclass
class Test(db.Model):
    id_test: int = db.Column(db.Integer, primary_key=True)
    id_tipo_test: int = db.Column(db.Integer, nullable=False)
    tipo_test: str = db.Column(db.String(50), nullable=False)

    def __init__(self, id_tipo_test, tipo_test):
        self.id_tipo_test = id_tipo_test
        self.tipo_test = tipo_test
