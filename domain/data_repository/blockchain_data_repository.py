from typing import List
from abc import ABC, abstractmethod
from domain.model.block import Block


class BlockchainDataRepository(ABC):
    @abstractmethod
    def insert_block(self, block: Block):
        pass

    @abstractmethod
    def get_last_index(self) -> int:
        pass

    @abstractmethod
    def get_last_block(self) -> Block:
        pass

    @abstractmethod
    def get_chain(self) -> List[Block]:
        pass