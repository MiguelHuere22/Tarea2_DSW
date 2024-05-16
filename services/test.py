from flask import Blueprint, request, jsonify
from model.test import Test
from utils.db import db

# Crea un Blueprint para las operaciones de Test
tests = Blueprint('tests',__name__)

# Ruta para obtener un mensaje básico
@tests.route('/tests/v1', methods=['GET'])
def getMensaje():
    result = {
        "data": "Hola, tests"
    }
    return jsonify(result)

# Ruta para listar todos los Tests
@tests.route('/tests/v1/listar', methods=['GET'])
def getTests():
      result={}
      tests=Test.query.all()    
      result["data"]=tests
      result["status_code"]=200
      result["msg"]="Se recupero los tipos de tests sin inconvenientes"
      return jsonify(result),200