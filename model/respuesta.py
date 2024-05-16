from utils.db import db
from dataclasses import dataclass

@dataclass
class Respuesta(db.Model):
    id_respuesta: int = db.Column(db.Integer, primary_key=True)
    respuesta_usuario: str = db.Column(db.String(2), nullable=False)
    pregunta_id: int = db.Column(db.Integer, db.ForeignKey('pregunta.id_pregunta'), nullable=False)
    id_estudiante: int = db.Column(db.Integer, db.ForeignKey('estudiante.id_estudiante'), nullable=False)

    def __init__(self, respuesta_usuario, pregunta_id, id_estudiante):
        self.respuesta_usuario = respuesta_usuario
        self.pregunta_id = pregunta_id
        self.id_estudiante = id_estudiante