import datetime
from .use_case import UseCase
from domain.model.block import Block

class CreateBlockUC(UseCase):
    def __init__(self, blockchain_repository):
        self.blockchain_repository = blockchain_repository

    def execute(self, params):
        last_index = self.blockchain_repository.get_last_index()
        block = Block(
            index = last_index + 1,
            timestamp = str(datetime.datetime.now()),
            proof = params.proof,
            previous_hash = params.previous_hash
        )
        self.blockchain_repository.insert_block(block)
        return block

    
class CreateBlockUCParams:
    def __init__(self, proof, previous_hash):
        self.proof = proof
        self.previous_hash = previous_hash