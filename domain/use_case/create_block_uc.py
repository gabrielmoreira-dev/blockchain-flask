from dataclasses import dataclass
import datetime
from . import UseCase
from domain.data_repository.blockchain_data_repository import BlockchainDataRepository
from domain.data_repository.mempool_data_repository import MempoolDataRepository
from domain.model.block import Block


@dataclass
class CreateBlockUCParams:
    proof: str
    previous_hash: str


class CreateBlockUC(UseCase):
    def __init__(self, blockchain_repository: BlockchainDataRepository,
                 mempool_data_repository: MempoolDataRepository):
        self.blockchain_repository = blockchain_repository
        self.mempool_data_repository = mempool_data_repository

    def execute(self, params: CreateBlockUCParams) -> Block:
        last_index = self.blockchain_repository.get_last_index()
        transactions = self.mempool_data_repository.get_transactions()
        block = Block(index=last_index + 1,
                      timestamp=str(datetime.datetime.now()),
                      proof=params.proof,
                      previous_hash=params.previous_hash,
                      transactions=transactions)
        self.blockchain_repository.insert_block(block)
        self.mempool_data_repository.clear_transactions()
        return block
