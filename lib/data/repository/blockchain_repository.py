from domain.data_repository.blockchain_data_repository import BlockchainDataRepository
from domain.model.block import Block
from lib.data.local.data_source.blockchain_lds import BlockchainLDS


class BlockchainRepository(BlockchainDataRepository):
    def __init__(self, blockchain_lds: BlockchainLDS):
        self.blockchain_lds = blockchain_lds

    def insert_block(self, block: Block):
        self.blockchain_lds.insert_block(block)

    def get_last_index(self):
        return self.blockchain_lds.get_last_index()

    def get_last_block(self):
        return self.blockchain_lds.get_last_block()

    def get_chain(self):
        return self.blockchain_lds.get_chain()