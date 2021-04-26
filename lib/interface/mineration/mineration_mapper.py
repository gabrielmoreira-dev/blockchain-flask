class MinerationMapper:
    def toVM(block):
        return {
            'message': 'Congratulations, you just mined a block!',
            'index': block.index,
            'timestamp': block.timestamp,
            'proof': block.proof,
            'previous_hash': block.previous_hash
        }