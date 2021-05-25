from domain.model.blockchain import Blockchain
from . import ValidationUseCase
from domain.data_repository.blockchain_data_repository import BlockchainDataRepository
from domain.data_repository.network_data_repository import NetworkDataRepository


class ReplaceBlockchainUC(ValidationUseCase):
    def __init__(self, blockchain_repository: BlockchainDataRepository,
                 network_repository: NetworkDataRepository):
        self.blockchain_repository = blockchain_repository
        self.network_repository = network_repository

    def execute(self) -> bool:
        network = self.network_repository.get_nodes()
        longest_chain = None
        local_blockchain = self.blockchain_repository.get_local_blockchain()
        max_length = local_blockchain.length
        for node in network:
            remote_blockchain = self.blockchain_repository.get_remote_blockchain(
                address=node.address)
            is_chain_longest = self._compare_nodes(
                blockchain=remote_blockchain, max_length=max_length)
            if is_chain_longest:
                max_length = remote_blockchain.length
                longest_chain = remote_blockchain.chain
        if longest_chain:
            self.blockchain_repository.set_local_blockchain(longest_chain)
            return True
        return False

    def _compare_nodes(self, blockchain: Blockchain, max_length: int):
        is_chain_valid = self.validate_chain(blockchain.chain)
        if blockchain.length > max_length and is_chain_valid:
            return True
        return False
