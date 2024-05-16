from flask import Blueprint, request, jsonify
from model.area import Area
from utils.db import db


areas=Blueprint('areas',__name__)

@areas.route('/areas/v1',methods=['GET'])
def getMensaje():
    result={}
    result["data"]='Hola , Areas'
    return jsonify(result)
#-------------------------------------------------------------

@areas.route('/areas/v1/listar',methods=['GET'])
def getAreas():
    result={}
    areas=Area.query.all()    
    result["data"]=areas
    result["status_code"]=200
    result["msg"]="Se recupero la lista de Areas sin inconvenientes"
    return jsonify(result),200
#---------------------------------------------------------------