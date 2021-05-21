from dataclasses import dataclass
from urllib.parse import urlparse
from . import UseCase
from domain.data_repository.network_data_repository import NetworkDataRepository
from domain.model.node import Node


@dataclass
class AddNodeUCParams:
    url: str


class AddNodeUC(UseCase):
    def __init__(self, network_data_repository: NetworkDataRepository):
        self.network_data_repository = network_data_repository

    def execute(self, params: AddNodeUCParams):
        parsed_url = urlparse(params.url)
        node = Node(address=parsed_url.netloc)
        self.network_data_repository.insert_node(node)
