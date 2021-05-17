from flask import Blueprint, jsonify
from .validation_factory import ValidationFactory

validation = Blueprint('validation', __name__, url_prefix='/validation')


@validation.route('/', methods=['GET'])
def validate_chain():
    validation_controller = ValidationFactory.makeController()
    response = validation_controller.validate_chain()
    return jsonify(response), 200