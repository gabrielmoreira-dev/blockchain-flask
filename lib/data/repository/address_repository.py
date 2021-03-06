from domain.data_repository.address_data_repository import AddressDataRepository
from lib.data.local.data_source.address_lds import AddressLDS


class AddressRepository(AddressDataRepository):
    def __init__(self, address_lds: AddressLDS):
        self.address_lds = address_lds

    def get_address(self) -> str:
        return self.address_lds.get_address()