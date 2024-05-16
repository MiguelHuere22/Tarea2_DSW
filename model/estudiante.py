from utils.db import db
from dataclasses import dataclass

@dataclass
class Estudiante(db.Model):
    id_estudiante: int = db.Column(db.Integer, primary_key=True)
    nombre: str = db.Column(db.String(255), nullable=False)
    apellido: str = db.Column(db.String(255), nullable=False)
    sexo: str = db.Column(db.CHAR(1), nullable=True)
    correo: str = db.Column(db.String(255), unique=True, nullable=True)
    telefono: str = db.Column(db.String(9), unique=True, nullable=True)

    def __init__(self, nombre, apellido, sexo, correo, telefono):
        self.Nombre = nombre
        self.Apellido = apellido
        self.Sexo = sexo
        self.Correo = correo
        self.Telefono = telefono