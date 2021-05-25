from abc import ABC, abstractmethod
from typing import List
from domain.model.block import Block
from domain.model.blockchain import Blockchain


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
    def get_local_blockchain(self) -> Blockchain:
        pass

    @abstractmethod
    def set_local_blockchain(self, chain: List[Block]):
        pass

    @abstractmethod
    def get_remote_blockchain(self, address: str) -> Blockchain:
        pass