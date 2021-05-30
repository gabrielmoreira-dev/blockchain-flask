from abc import ABC, abstractmethod


class AddressDataRepository(ABC):
    @abstractmethod
    def get_address(self) -> str:
        pass
