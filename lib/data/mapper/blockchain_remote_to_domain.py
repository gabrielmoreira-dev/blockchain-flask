from domain.model.block import Block
from domain.model.blockchain import Blockchain
from domain.model.transaction import Transaction


class BlockchainRemoteToDomain:
    def toDM(data):
        length = data["length"]
        chain = []
        for block in data["chain"]:
            transactions = []
            for transaction in block["transactions"]:
                transactions.append(
                    Transaction(sender=transaction["sender"],
                                receiver=transaction["receiver"],
                                amount=transaction["amount"]))
            chain.append(
                Block(index=block["index"],
                      timestamp=block["timestamp"],
                      proof=block["proof"],
                      previous_hash=block["previous_hash"],
                      transactions=transactions))
        return Blockchain(chain, length)
