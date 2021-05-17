from uuid import uuid4
from . import UseCase
from domain.data_repository.address_data_repository import AddressDataRepository


class SetNodeAddressUC(UseCase):
    def __init__(self, address_repository: AddressDataRepository):
        self.address_repository = address_repository

    def execute(self):
        address = str(uuid4()).replace('-', '')
        self.address_repository.set_node_address(address)
