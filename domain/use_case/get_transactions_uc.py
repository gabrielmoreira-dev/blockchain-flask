from typing import List
from . import UseCase
from domain.data_repository.mempool_data_repository import MempoolDataRepository
from domain.model.transaction import Transaction


class GetTransactionsUC(UseCase):
    def __init__(self, mempool_data_repository: MempoolDataRepository):
        self.mempool_data_repository = mempool_data_repository

    def execute(self) -> List[Transaction]:
        return self.mempool_data_repository.get_transactions()