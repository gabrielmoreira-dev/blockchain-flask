from lib.api import transaction
from flask import Blueprint, jsonify, request
from .node_factory import NodeFactory

node = Blueprint('node', __name__, url_prefix='/node')


@node.route('', methods=['POST'])
def connect_node():
    json = request.get_json()
    nodes = json.get('nodes')
    if nodes is None:
        return "No node provided", 400
    node_controller = NodeFactory.makeController()
    response = node_controller.add_nodes(nodes)
    return jsonify(response), 201
