from typing import List
from . import UseCase
from domain.data_repository.network_data_repository import NetworkDataRepository
from domain.model.node import Node


class GetNodesUC(UseCase):
    def __init__(self, network_data_repository: NetworkDataRepository):
        self.network_data_repository = network_data_repository

    def execute(self) -> List[Node]:
        return self.network_data_repository.get_nodes()