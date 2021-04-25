class Block:
    def __init__(self, index, timestamp, proof, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.proof = proof
        self.previous_hash = previous_hash
