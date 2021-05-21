from typing import List
from abc import ABC, abstractmethod
from domain.model.node import Node


class NetworkDataRepository(ABC):
    @abstractmethod
    def insert_node(self, node: Node):
        pass

    @abstractmethod
    def get_nodes(self) -> List[Node]:
        pass