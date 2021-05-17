from dataclasses import dataclass
from . import UseCase
from domain.data_repository.mempool_data_repository import MempoolDataRepository
from domain.model.transaction import Transaction


@dataclass
class AddTransactionUCParams:
    sender: str
    receiver: str
    amount: float


class AddTransactionUC(UseCase):
    def __init__(self, mempool_data_repository: MempoolDataRepository):
        self.mempool_data_repository = mempool_data_repository

    def execute(self, params: AddTransactionUCParams):
        transaction = Transaction(sender=params.sender,
                                  receiver=params.receiver,
                                  amount=params.amount)
        self.mempool_data_repository.insert_transaction(transaction)