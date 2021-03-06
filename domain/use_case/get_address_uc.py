from . import UseCase
from domain.data_repository.address_data_repository import AddressDataRepository


class GetAddressUC(UseCase):
    def __init__(self, address_repository: AddressDataRepository):
        self.address_repository = address_repository

    def execute(self) -> str:
        return self.address_repository.get_address()
