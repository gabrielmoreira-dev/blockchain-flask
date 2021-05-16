from flask import Blueprint, jsonify
from .mineration_factory import MinerationFactory

mineration = Blueprint('mineration', __name__, url_prefix='/mine-block')


@mineration.route('/', methods=['GET'])
def mine_block():
    mineration_controller = MinerationFactory.makeController()
    response = mineration_controller.mine_block()
    return jsonify(response), 200