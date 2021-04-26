class ChainMapper:
    def toVM(chain):
        blockchain = []
        for block in chain:
            blockchain.append(ChainMapper._convertBlockToVM(block))
        return {'chain': blockchain, 'length': len(chain)}

    def _convertBlockToVM(block):
        return {
            'index': block.index,
            'timestamp': block.timestamp,
            'proof': block.proof,
            'previous_hash': block.previous_hash
        }