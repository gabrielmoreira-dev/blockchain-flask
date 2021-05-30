from typing import List
from . import ValidationUseCase
from domain.data_repository.blockchain_data_repository import BlockchainDataRepository
from domain.model.block import Block


class ValidateChainUC(ValidationUseCase):
    def __init__(self, blockchain_repository: BlockchainDataRepository):
        self.blockchain_repository = blockchain_repository

    def execute(self) -> bool:
        chain = self.blockchain_repository.get_local_blockchain()
        return self.validate_chain(chain)