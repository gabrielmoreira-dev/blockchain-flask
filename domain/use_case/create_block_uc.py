from typing import List
from dataclasses import dataclass
import datetime
from . import UseCase
from domain.data_repository.blockchain_data_repository import BlockchainDataRepository
from domain.model.block import Block
from domain.model.transaction import Transaction


@dataclass
class CreateBlockUCParams:
    proof: str
    previous_hash: str
    transactions: List[Transaction]


class CreateBlockUC(UseCase):
    def __init__(self, blockchain_repository: BlockchainDataRepository):
        self.blockchain_repository = blockchain_repository

    def execute(self, params: CreateBlockUCParams):
        last_index = self.blockchain_repository.get_last_index()
        block = Block(index=last_index + 1,
                      timestamp=str(datetime.datetime.now()),
                      proof=params.proof,
                      previous_hash=params.previous_hash,
                      transactions=params.transactions)
        self.blockchain_repository.insert_block(block)
        return block
