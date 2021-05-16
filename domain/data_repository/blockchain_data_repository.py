from abc import ABC, abstractmethod
from domain.model.block import Block


class BlockchainDataRepository(ABC):
    @abstractmethod
    def insert_block(self, block: Block):
        pass

    @abstractmethod
    def get_last_index(self):
        pass

    @abstractmethod
    def get_last_block(self):
        pass

    @abstractmethod
    def get_chain(self):
        pass