from domain.use_case.get_local_blockchain_uc import GetLocalBlockchainUC
from .chain_mapper import ChainMapper


class ChainController:
    def __init__(self, get_local_blockchain_uc: GetLocalBlockchainUC):
        self.get_local_blockchain_uc = get_local_blockchain_uc

    def get_chain(self):
        blockchain = self.get_local_blockchain_uc.execute()
        return ChainMapper.toDict(blockchain.chain)