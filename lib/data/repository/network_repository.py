from typing import List
from domain.data_repository.network_data_repository import NetworkDataRepository
from domain.model.node import Node
from lib.data.local.data_source.network_lds import NetworkLDS


class NetworkRepository(NetworkDataRepository):
    def __init__(self, network_lds: NetworkLDS):
        self.network_lds = network_lds

    def insert_node(self, node: Node):
        self.network_lds.insert_node(node.address)

    def get_nodes(self) -> List[Node]:
        addresses = self.network_lds.get_nodes()
        nodes = map(self._get_node, addresses)
        return list(nodes)

    def _get_node(self, address: str):
        return Node(address)