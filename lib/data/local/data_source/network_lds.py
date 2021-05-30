from typing import List


class NetworkLDS:
    def __init__(self):
        self.nodes = set()

    def insert_node(self, address: str):
        self.nodes.add(address)

    def get_nodes(self) -> List[str]:
        return list(self.nodes)
