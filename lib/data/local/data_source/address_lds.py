from uuid import uuid4


class AddressLDS:
    def __init__(self):
        address = str(uuid4()).replace('-', '')
        self.node_address = address

    def get_address(self) -> str:
        return self.node_address