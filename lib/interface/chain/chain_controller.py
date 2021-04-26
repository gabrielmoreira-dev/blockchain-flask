from domain.use_case.get_blockchain_uc import GetBlockchainUCParams
from .chain_mapper import ChainMapper


class ChainController:
    def __init__(self, get_blockchain_uc):
        self.get_blockchain_uc = get_blockchain_uc

    def get_chain(self):
        params = GetBlockchainUCParams()
        blockchain = self.get_blockchain_uc.execute(params)
        return ChainMapper.toVM(blockchain.chain)