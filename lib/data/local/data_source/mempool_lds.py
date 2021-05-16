from domain.model.transaction import Transaction


class MempoolLDS:
    def __init__(self):
        self.transactions = []

    def insert_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def get_transactions(self):
        return self.transactions

    def clear_transactions(self):
        self.transactions = []