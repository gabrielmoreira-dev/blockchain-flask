from domain.data_repository.mempool_data_repository import MempoolDataRepository
from domain.model.transaction import Transaction
from lib.data.local.data_source.mempool_lds import MempoolLDS


class MempoolRepository(MempoolDataRepository):
    def __init__(self, mempool_lds: MempoolLDS):
        self.mempool_lds = mempool_lds

    def insert_transaction(self, transaction: Transaction):
        self.mempool_lds.insert_transaction(transaction)

    def get_transactions(self):
        return self.mempool_lds.get_transactions()

    def clear_transactions(self):
        self.mempool_lds.clear_transactions()