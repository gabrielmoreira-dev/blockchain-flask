from lib.provider import blockchain_repository, mempool_repository
from domain.use_case.add_transaction_uc import AddTransactionUC
from domain.use_case.get_previous_block_uc import GetPreviousBlockUC
from .transaction_controller import TransactionController


class TransactionFactory:
    def makeController() -> TransactionController:
        add_transaction_uc = AddTransactionUC(mempool_repository)
        get_previous_block_uc = GetPreviousBlockUC(blockchain_repository)
        return TransactionController(
            add_transaction_uc=add_transaction_uc,
            get_previous_block_uc=get_previous_block_uc)
