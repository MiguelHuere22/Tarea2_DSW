from utils.db import db
from dataclasses import dataclass

@dataclass
class TestBeck(db.Model):
    id_beck: int = db.Column(db.Integer, primary_key=True)
    nombre: str = db.Column(db.String(255), nullable=False)
    numero_preguntas: int = db.Column(db.Integer, nullable=False)
    descripcion: str = db.Column(db.Text, nullable=True)

    def __init__(self, nombre, numero_preguntas, descripcion=None):
        self.nombre = nombre
        self.numero_preguntas = numero_preguntas
        self.descripcion = descripcion
