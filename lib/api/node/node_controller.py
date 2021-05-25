from typing import List
from domain.use_case.add_node_uc import AddNodeUC, AddNodeUCParams
from domain.use_case.get_nodes_uc import GetNodesUC
from .node_mapper import NodeMapper


class NodeController:
    def __init__(self, add_node_uc: AddNodeUC, get_nodes_uc: GetNodesUC):
        self.add_node_uc = add_node_uc
        self.get_nodes_uc = get_nodes_uc

    def add_nodes(self, nodes: List[str]):
        for node in nodes:
            params = AddNodeUCParams(url=node)
            self.add_node_uc.execute(params)
        current_nodes = self._get_nodes()
        return NodeMapper.toDict(current_nodes)

    def _get_nodes(self):
        return self.get_nodes_uc.execute()