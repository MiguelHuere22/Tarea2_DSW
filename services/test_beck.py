from flask import Blueprint, jsonify
from model.test_beck import TestBeck
from utils.db import db

test_beck_bp = Blueprint('test_beck_bp', __name__)

@test_beck_bp.route('/test_beck/v1', methods=['GET'])
def getMensaje():
    result = {"data": 'Hola, Test Beck'}
    return jsonify(result)

# -------------------------------------------------------------

@test_beck_bp.route('/test_beck/v1/listar', methods=['GET'])
def getTestBeck():
    tests_beck = TestBeck.query.all()
    result = {
        "data": [test.__dict__ for test in tests_beck],
        "status_code": 200,
        "msg": "Se recuperó la lista de Tests Beck sin inconvenientes"
    }
    for test in result["data"]:
        test.pop('_sa_instance_state', None)  # Eliminar metadata de SQLAlchemy
    return jsonify(result), 200
