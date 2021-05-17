class AddressLDS:
    def __init__(self):
        self.node_address = None

    def set_node_address(self, address: str):
        self.node_address = address

    def get_node_address(self):
        return self.node_address