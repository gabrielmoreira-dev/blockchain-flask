from domain.data_repository.blockchain_data_repository import BlockchainDataRepository

class BlockchainRepository(BlockchainDataRepository):
    def __init__(self):
        self.chain = []
    
    def insert_block(self, block):
        chain.append(block)

    def get_last_index(self):
        return len(self.chain)

    def get_last_block(self):
        return self.chain[-1]

    def get_blockchain(self):
        return self.chain