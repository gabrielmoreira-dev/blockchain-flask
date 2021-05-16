from .chain_mapper import ChainMapper


class ChainController:
    def __init__(self, get_blockchain_uc):
        self.get_blockchain_uc = get_blockchain_uc

    def get_chain(self):
        blockchain = self.get_blockchain_uc.execute()
        return ChainMapper.toDict(blockchain.chain)