from flask import Blueprint, jsonify
from .chain_factory import ChainFactory

chain = Blueprint('chain', __name__, url_prefix='/chain')


@chain.route('/', methods=['GET'])
def get_chain():
    chain_controller = ChainFactory.makeController()
    response = chain_controller.get_chain()
    return jsonify(response), 200