from typing import List
from domain.model.node import Node


class NodeMapper:
    def toDict(nodes: List[Node]):
        addresses = list(map(NodeMapper._get_address, nodes))
        message = 'All the nodes were added'
        return {'message': message, 'nodes': addresses}

    def _get_address(node: Node):
        return node.address
