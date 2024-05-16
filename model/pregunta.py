from utils.db import db
from dataclasses import dataclass

@dataclass
class Pregunta(db.Model):
    id_pregunta: int = db.Column(db.Integer, primary_key=True)
    texto: str = db.Column(db.Text, nullable=False)
    area_id: int = db.Column(db.Integer, db.ForeignKey('area.id_area'), nullable=False)
    test_id: int = db.Column(db.Integer, db.ForeignKey('test.id_test'), nullable=False)

    def __init__(self, texto, area_id, test_id):
        self.texto = texto
        self.area_id = area_id
        self.test_id = test_id