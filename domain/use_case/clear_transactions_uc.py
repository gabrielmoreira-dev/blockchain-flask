from . import UseCase
from domain.data_repository.mempool_data_repository import MempoolDataRepository


class ClearTransactionsUC(UseCase):
    def __init__(self, mempool_data_repository: MempoolDataRepository):
        self.mempool_data_repository = mempool_data_repository

    def execute(self):
        return self.mempool_data_repository.clear_transactions()