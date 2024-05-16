from flask import Blueprint, request, jsonify
from model.respuesta import Respuesta
from utils.db import db

respuestas=Blueprint('respuestas',__name__)

@respuestas.route('/respuestas/v1',methods=['GET'])
def getMensaje():
    result={}
    result["data"]='Hola , Respuestas'
    return jsonify(result)
#-------------------------------------------------------------

@respuestas.route('/respuestas/v1/listar',methods=['GET'])
def getRespuestas():
    result={}
    respuestas=Respuesta.query.all()    
    result["data"]=respuestas
    result["status_code"]=200
    result["msg"]="Se recupero la lista de Respuestas sin inconvenientes"
    return jsonify(result),200
#---------------------------------------------------------------


# Método insert para Respuesta
@respuestas.route('/respuestas/v1/insert', methods=['POST'])
def insert():
    result = {}
    respuestas_data = request.get_json()  # Esto debería ser una lista de diccionarios

    if not isinstance(respuestas_data, list):  # Verifica si el payload es una lista
        return jsonify({"status_code": 400, "msg": "Formato de datos incorrecto, se espera una lista"}), 400

    nuevas_respuestas = []
    for data in respuestas_data:
        respuesta_usuario = data.get('respuesta_usuario')
        pregunta_id = data.get('pregunta_id')
        id_estudiante = data.get('id_estudiante')

        if not respuesta_usuario or not pregunta_id or not id_estudiante:
            return jsonify({"status_code": 400, "msg": "Faltan datos requeridos en algunos items"}), 400

        # Crear el objeto Respuesta
        respuesta = Respuesta(respuesta_usuario, pregunta_id, id_estudiante)
        db.session.add(respuesta)
        nuevas_respuestas.append(respuesta)

    db.session.commit()  # Realiza el commit de todas las respuestas juntas

    result["data"] = [respuesta for respuesta in nuevas_respuestas]  # Asegúrate de que Respuesta tiene un método to_dict()
    result["status_code"] = 201
    result["msg"] = "Respuestas agregadas con éxito"
    return jsonify(result), 201


@respuestas.route('/respuestas/v1/update', methods=['POST'])
def update():
    result = {}
    respuestas_data = request.get_json()

    if not isinstance(respuestas_data, list):  # Verifica si el payload es una lista
        return jsonify({"status_code": 400, "msg": "Formato de datos incorrecto, se espera una lista"}), 400

    actualizadas_respuestas = []
    for data in respuestas_data:
        id_respuesta = data.get('id_respuesta')
        respuesta_usuario = data.get('respuesta_usuario')
        pregunta_id = data.get('pregunta_id')
        id_estudiante = data.get('id_estudiante')

        if not all([id_respuesta, respuesta_usuario, pregunta_id, id_estudiante]):
            return jsonify({"status_code": 400, "msg": "Faltan datos requeridos en algunos items"}), 400

        respuesta = Respuesta.query.get(id_respuesta)
        if not respuesta:
            continue  # Si la respuesta no existe, salta a la siguiente

        respuesta.respuesta_usuario = respuesta_usuario
        respuesta.pregunta_id = pregunta_id
        respuesta.id_estudiante = id_estudiante
        actualizadas_respuestas.append(respuesta)

    db.session.commit()  # Realiza el commit de todas las actualizaciones juntas

    result["data"] = [respuesta for respuesta in actualizadas_respuestas]  # Devuelve los IDs de las respuestas actualizadas
    result["status_code"] = 202
    result["msg"] = "Respuestas actualizadas con éxito"
    return jsonify(result), 202