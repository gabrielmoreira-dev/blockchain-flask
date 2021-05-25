from lib.provider import blockchain_repository
from domain.use_case.get_local_blockchain_uc import GetLocalBlockchainUC
from .chain_controller import ChainController


class ChainFactory:
    def makeController() -> ChainController:
        get_local_blockchain_uc = GetLocalBlockchainUC(blockchain_repository)
        return ChainController(get_local_blockchain_uc)