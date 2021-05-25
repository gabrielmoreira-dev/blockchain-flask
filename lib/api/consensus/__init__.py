from flask import Blueprint, jsonify
from .consensus_factory import ConsensusFactory

consensus = Blueprint('consensus', __name__, url_prefix='/replace-chain')


@consensus.route('', methods=['GET'])
def replace_chain():
    consensus_controller = ConsensusFactory.makeController()
    response = consensus_controller.replace_chain()
    return jsonify(response), 200