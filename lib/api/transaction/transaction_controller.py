from domain.use_case.add_transaction_uc import AddTransactionUC, AddTransactionUCParams
from domain.use_case.get_previous_block_uc import GetPreviousBlockUC
from .transaction_mapper import TransactionMapper


class TransactionController:
    def __init__(self, add_transaction_uc: AddTransactionUC,
                 get_previous_block_uc: GetPreviousBlockUC):
        self.add_transaction_uc = add_transaction_uc
        self.get_previous_block_uc = get_previous_block_uc

    def add_transaction(self, sender: str, receiver: str, amount: float):
        params = AddTransactionUCParams(sender=sender,
                                        receiver=receiver,
                                        amount=amount)
        self.add_transaction_uc.execute(params)
        index = self._get_index()
        return TransactionMapper.toDict(index)

    def _get_index(self):
        previous_block = self.get_previous_block_uc.execute()
        return previous_block.index + 1
