from flask import Blueprint, request, jsonify
from model.estudiante import Estudiante
from utils.db import db


estudiantes=Blueprint('estudiantes',__name__)

@estudiantes.route('/estudiantes/v1',methods=['GET'])
def getMensaje():
    result={}
    result["data"]='Hola , estudiantes'
    return jsonify(result)
#-------------------------------------------------------------

@estudiantes.route('/estudiantes/v1/listar',methods=['GET'])
def getEstudiantes():
    result={}
    estudiantes=Estudiante.query.all()    
    result["data"]=estudiantes
    result["status_code"]=200
    result["msg"]="Se recupero los estudiantes sin inconvenientes"
    return jsonify(result),200
#---------------------------------------------------------------