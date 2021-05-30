from lib.provider import blockchain_repository, network_repository
from domain.use_case.get_blockchain_uc import GetBlockchainUC
from domain.use_case.replace_blockchain_uc import ReplaceBlockchainUC
from .consensus_controller import ConsensusController


class ConsensusFactory:
    def makeController() -> ConsensusController:
        get_blockchain_uc = GetBlockchainUC(blockchain_repository)
        replace_blockchain_uc = ReplaceBlockchainUC(blockchain_repository,
                                                    network_repository)
        return ConsensusController(get_blockchain_uc, replace_blockchain_uc)
