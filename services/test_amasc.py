from flask import Blueprint, jsonify
from model.test_amasc import TestAMASC
from utils.db import db

test_amasc_bp = Blueprint('test_amasc_bp', __name__)

@test_amasc_bp.route('/test_amasc/v1', methods=['GET'])
def getMensaje():
    result = {"data": 'Hola, Test AMASC'}
    return jsonify(result)

# -------------------------------------------------------------

@test_amasc_bp.route('/test_amasc/v1/listar', methods=['GET'])
def getTestAMASC():
    tests_amasc = TestAMASC.query.all()
    result = {
        "data": [test.__dict__ for test in tests_amasc],
        "status_code": 200,
        "msg": "Se recuperó la lista de Tests AMASC sin inconvenientes"
    }
    for test in result["data"]:
        test.pop('_sa_instance_state', None)  # Eliminar metadata de SQLAlchemy
    return jsonify(result), 200
