from flask import Flask, jsonify
from lib.interface.validation.validation_controller import ValidationController
from lib.interface.mineration.mineration_controller import MinerationController
from lib.interface.chain.chain_controller import ChainController
from lib.data.repository.blockchain_repository import BlockchainRepository
from domain.use_case.create_block_uc import CreateBlockUC, CreateBlockUCParams
from domain.use_case.get_blockchain_uc import GetBlockchainUC, GetBlockchainUCParams
from domain.use_case.get_hash_uc import GetHashUC, GetHashUCParams
from domain.use_case.get_previous_block_uc import GetPreviousBlockUC, GetPreviousBlockUCParams
from domain.use_case.get_proof_of_work_uc import GetProofOfWorkUC, GetProofOfWorkUCParams
from domain.use_case.validate_chain_uc import ValidateChainUC, ValidateChainUCParams

app = Flask(__name__)
blockchain_repository = BlockchainRepository()
create_block_uc = CreateBlockUC(blockchain_repository)
get_blockchain_uc = GetBlockchainUC(blockchain_repository)
get_hash_uc = GetHashUC()
get_previous_block_uc = GetPreviousBlockUC(blockchain_repository)
get_proof_of_work_uc = GetProofOfWorkUC()
validate_chain_uc = ValidateChainUC(blockchain_repository)

validation_controller = ValidationController(validate_chain_uc)
mineration_controller = MinerationController(get_previous_block_uc,
                                             get_proof_of_work_uc, get_hash_uc,
                                             create_block_uc)
chain_controller = ChainController(get_blockchain_uc)

params = CreateBlockUCParams(proof=1, previous_hash='0')
create_block_uc.execute(params)


@app.route('/mine-block', methods=['GET'])
def mine_block():
    response = mineration_controller.mine_block()
    return jsonify(response), 200


@app.route('/chain', methods=['GET'])
def get_blockchain():
    response = chain_controller.get_chain()
    return jsonify(response), 200


@app.route('/is-valid', methods=['GET'])
def verify_chain_is_valid():
    response = validation_controller.validate_chain()
    return jsonify(response), 200


if __name__ == "__main__":
    app.run(debug=True)