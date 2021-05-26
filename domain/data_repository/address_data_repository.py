from abc import ABC, abstractmethod


class AddressDataRepository(ABC):
    @abstractmethod
    def get_node_address(self) -> str:
        pass
