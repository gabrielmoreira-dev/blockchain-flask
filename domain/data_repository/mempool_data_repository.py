from typing import List
from abc import ABC, abstractmethod
from domain.model.transaction import Transaction


class MempoolDataRepository(ABC):
    @abstractmethod
    def insert_transaction(self, transaction: Transaction):
        pass

    @abstractmethod
    def get_transactions(self) -> List[Transaction]:
        pass

    @abstractmethod
    def clear_transactions(self):
        pass