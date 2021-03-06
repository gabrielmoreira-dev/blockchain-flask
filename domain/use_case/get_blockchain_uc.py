from . import UseCase
from domain.model.blockchain import Blockchain
from domain.data_repository.blockchain_data_repository import BlockchainDataRepository


class GetBlockchainUC(UseCase):
    def __init__(self, blockchain_repository: BlockchainDataRepository):
        self.blockchain_repository = blockchain_repository

    def execute(self) -> Blockchain:
        return self.blockchain_repository.get_local_blockchain()