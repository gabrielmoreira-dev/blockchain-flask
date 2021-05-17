from abc import ABC, abstractmethod


class AddressDataRepository(ABC):
    @abstractmethod
    def set_node_address(self, address: str):
        pass

    @abstractmethod
    def get_node_address(self):
        pass
