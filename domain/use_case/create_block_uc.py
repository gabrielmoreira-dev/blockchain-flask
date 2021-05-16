import datetime
from . import UseCase
from domain.model.block import Block
from domain.data_repository.blockchain_data_repository import BlockchainDataRepository


class CreateBlockUCParams:
    def __init__(self, proof: str, previous_hash: str):
        self.proof = proof
        self.previous_hash = previous_hash


class CreateBlockUC(UseCase):
    def __init__(self, blockchain_repository: BlockchainDataRepository):
        self.blockchain_repository = blockchain_repository

    def execute(self, params: CreateBlockUCParams):
        last_index = self.blockchain_repository.get_last_index()
        block = Block(index=last_index + 1,
                      timestamp=str(datetime.datetime.now()),
                      proof=params.proof,
                      previous_hash=params.previous_hash)
        self.blockchain_repository.insert_block(block)
        return block
