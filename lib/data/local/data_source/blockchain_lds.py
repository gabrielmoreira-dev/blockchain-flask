from domain.model.block import Block


class BlockchainLDS:
    def __init__(self):
        self.chain = []

    def insert_block(self, block: Block):
        self.chain.append(block)

    def get_last_index(self):
        return len(self.chain)

    def get_last_block(self):
        return self.chain[-1]

    def get_chain(self):
        return self.chain