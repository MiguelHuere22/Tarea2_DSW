from flask import Blueprint, request, jsonify
from model.pregunta import Pregunta
from utils.db import db


preguntas=Blueprint('preguntas',__name__)

@preguntas.route('/preguntas/v1',methods=['GET'])
def getMensaje():
    result={}
    result["data"]='Hola , Preguntas'
    return jsonify(result)
#-------------------------------------------------------------

@preguntas.route('/preguntas/v1/listar',methods=['GET'])
def getPreguntas():
    result={}
    preguntas=Pregunta.query.all()    
    result["data"]=preguntas
    result["status_code"]=200
    result["msg"]="Se recupero la lista de Preguntas sin inconvenientes"
    return jsonify(result),200
#---------------------------------------------------------------