from lib.provider import network_repository
from domain.use_case.add_node_uc import AddNodeUC
from domain.use_case.get_nodes_uc import GetNodesUC
from .node_controller import NodeController


class NodeFactory:
    def makeController() -> NodeController:
        add_node_uc = AddNodeUC(network_repository)
        get_nodes_uc = GetNodesUC(network_repository)
        return NodeController(add_node_uc=add_node_uc,
                              get_nodes_uc=get_nodes_uc)
