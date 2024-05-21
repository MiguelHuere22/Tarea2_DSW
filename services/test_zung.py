from flask import Blueprint, jsonify
from model.test_zung import TestZung
from utils.db import db

test_zung_bp = Blueprint('test_zung_bp', __name__)

@test_zung_bp.route('/test_zung/v1', methods=['GET'])
def getMensaje():
    result = {"data": 'Hola, Test Zung'}
    return jsonify(result)

# -------------------------------------------------------------

@test_zung_bp.route('/test_zung/v1/listar', methods=['GET'])
def getTestZung():
    tests_zung = TestZung.query.all()
    result = {
        "data": [test.__dict__ for test in tests_zung],
        "status_code": 200,
        "msg": "Se recuperó la lista de Tests Zung sin inconvenientes"
    }
    for test in result["data"]:
        test.pop('_sa_instance_state', None)  # Eliminar metadata de SQLAlchemy
    return jsonify(result), 200
