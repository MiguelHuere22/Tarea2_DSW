from utils.db import db
from dataclasses import dataclass

@dataclass
class Test(db.Model):
    id_test: int = db.Column(db.Integer, primary_key=True)
    nombre: str = db.Column(db.String(255), nullable=False)
    fecha_creacion: str = db.Column(db.Date, nullable=False)

    def __init__(self, nombre, fecha_creacion):
        self.nombre = nombre
        self.fecha_creacion = fecha_creacion