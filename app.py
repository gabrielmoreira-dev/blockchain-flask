import datetime
import hashlib
import json
from flask import Flask, jsonify


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def get_proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = self.generate_proof_hash(
                new_proof, previous_proof)
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def generate_proof_hash(self, proof, previous_proof):
        operation = str(proof**2 - previous_proof**2)
        return hashlib.sha256(operation.encode()).hexdigest()

    def generate_block_hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def verify_chain_is_valid(self, chain):
        previous_block = chain[0]
        index = 1
        while index < len(chain):
            block = chain[index]
            if block['previous_hash'] != self.generate_block_hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = self.generate_proof_hash(proof, previous_proof)
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            index += 1
        return True


app = Flask(__name__)
blockchain = Blockchain()


@app.route('/mine-block', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.get_proof_of_work(previous_proof)
    previous_hash = blockchain.generate_block_hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {
        'message': 'Congratulations, you just mined a block!',
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }
    return jsonify(response), 200


@app.route('/chain', methods=['GET'])
def get_blockchain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200


@app.route('/is-valid', methods=['GET'])
def verify_chain_is_valid():
    is_valid = blockchain.verify_chain_is_valid(blockchain.chain)
    message = 'The blockchain is valid' if is_valid else 'The blockchain is not valid'
    response = {
        'message': message
    }
    return jsonify(response), 200


app.run(host='0.0.0.0', port=5000)
