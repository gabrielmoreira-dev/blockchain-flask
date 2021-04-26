from lib.provider import get_blockchain_uc
from .chain_controller import ChainController


class ChainFactory:
    def makeController():
        return ChainController(get_blockchain_uc)