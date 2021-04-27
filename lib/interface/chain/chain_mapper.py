import dataclasses


class ChainMapper:
    def toDict(chain):
        blockchain = []
        for block in chain:
            blockchain.append(dataclasses.asdict(block))
        return {'chain': blockchain, 'length': len(chain)}