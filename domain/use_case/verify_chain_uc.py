from .cryptographic_hash_use_case import CryptographicHashUseCase
from .proof_of_work_use_case import ProofOfWorkUseCase

class VerifyChainUC(CryptographicHashUseCase, ProofOfWorkUseCase):
    def __init__(self, blockchain_repository):
        self.blockchain_repository = blockchain_repository

    def execute(self, params):
        chain = self.blockchain_repository.get_chain()
        previous_block = chain[0]
        index = 1
        while index < len(chain):
            block = chain[index]
            hash_link_is_valid = self.verify_hash_link(block, previous_block)
            if hash_link_is_valid is False:
                return False
            proof_of_work_is_valid = self.verify_proof_of_work(block, previous_block)
            if proof_of_work_is_valid is False: 
                return False
            previous_block = block
            index += 1
        return True

    def verify_hash_link(self, block, previous_block):
        previous_hash = block.previous_hash
        if block.previous_hash != self.generate_block_hash(previous_block):
            return False
        else return True

    def verify_proof_of_work(self, block, previous_block):
        previous_proof = previous_block.proof
        proof = block.proof
        generated_hash = self.generate_proof_hash(proof, previous_proof)
        hash_resolves_puzzle = self.verify_hash(generated_hash)
        if hash_resolves_puzzle is False:
            return False
        else return True

class VerifyChainUCParams:
    pass