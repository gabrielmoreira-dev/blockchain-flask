from . import CryptographicHashUseCase, ProofOfWorkUseCase
from domain.data_repository.blockchain_data_repository import BlockchainDataRepository
from domain.model.block import Block


class ValidateChainUC(CryptographicHashUseCase, ProofOfWorkUseCase):
    def __init__(self, blockchain_repository: BlockchainDataRepository):
        self.blockchain_repository = blockchain_repository

    def execute(self) -> bool:
        chain = self.blockchain_repository.get_chain()
        previous_block = chain[0]
        index = 1
        while index < len(chain):
            block = chain[index]
            hash_link_is_valid = self.validate_hash_link(block, previous_block)
            if hash_link_is_valid is False:
                return False
            proof_of_work_is_valid = self.validate_proof_of_work(
                block, previous_block)
            if proof_of_work_is_valid is False:
                return False
            previous_block = block
            index += 1
        return True

    def validate_hash_link(self, block: Block, previous_block: Block) -> bool:
        previous_hash = block.previous_hash
        if previous_hash != self.generate_block_hash(previous_block):
            return False
        return True

    def validate_proof_of_work(self, block: Block,
                               previous_block: Block) -> bool:
        previous_proof = previous_block.proof
        proof = block.proof
        generated_hash = self.generate_proof_hash(proof, previous_proof)
        hash_resolves_puzzle = self.validate_hash(generated_hash)
        if hash_resolves_puzzle is False:
            return False
        return True