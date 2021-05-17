from flask import Blueprint, jsonify, request
from .transaction_factory import TransactionFactory

transaction = Blueprint('transaction', __name__, url_prefix='/transaction')


@transaction.route('/', methods=['POST'])
def add_transaction():
    json = request.get_json()
    keys = ['sender', 'receiver', 'amount']
    if not all(key in json for key in keys):
        return 'Missing parameters', 400
    transaction_controller = TransactionFactory.makeController()
    response = transaction_controller.add_transaction(
        sender=json['sender'],
        receiver=json['receiver'],
        amount=json['amount'])
    return jsonify(response), 201