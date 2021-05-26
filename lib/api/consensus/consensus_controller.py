from domain.use_case.get_blockchain_uc import GetBlockchainUC
from domain.use_case.replace_blockchain_uc import ReplaceBlockchainUC
from .consensus_mapper import ConsensusMapper


class ConsensusController:
    def __init__(self, get_blockchain_uc: GetBlockchainUC,
                 replace_blockchain_uc: ReplaceBlockchainUC):
        self.get_blockchain_uc = get_blockchain_uc
        self.replace_blockchain_uc = replace_blockchain_uc

    def replace_chain(self):
        is_replaced = self.replace_blockchain_uc.execute()
        blockchain = self.get_blockchain_uc.execute()
        return ConsensusMapper.toDict(chain=blockchain.chain,
                                      is_replaced=is_replaced)
