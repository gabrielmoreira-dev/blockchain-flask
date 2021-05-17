from . import UseCase
from domain.data_repository.blockchain_data_repository import BlockchainDataRepository
from domain.model.block import Block


class GetPreviousBlockUC(UseCase):
    def __init__(self, blockchain_repository: BlockchainDataRepository):
        self.blockchain_repository = blockchain_repository

    def execute(self) -> Block:
        return self.blockchain_repository.get_last_block()