from lib.provider import blockchain_repository
from domain.use_case.get_blockchain_uc import GetBlockchainUC
from .chain_controller import ChainController


class ChainFactory:
    def makeController() -> ChainController:
        get_blockchain_uc = GetBlockchainUC(blockchain_repository)
        return ChainController(get_blockchain_uc)