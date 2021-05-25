import json
import hashlib
from abc import ABC, abstractmethod
from typing import List
from domain.model.block import Block


class UseCase(ABC):
    @abstractmethod
    def execute(self, params):
        pass


class CryptographicHashUseCase(UseCase):
    def generate_block_hash(self, block: Block):
        encoded_block = json.dumps(
            block,
            default=lambda o: o.__dict__,
            sort_keys=True,
        ).encode()
        return hashlib.sha256(encoded_block).hexdigest()


class ProofOfWorkUseCase(UseCase):
    _puzzle_rule = '0000'

    def generate_proof_hash(self, proof: int, previous_proof: int):
        operation = str(proof**2 - previous_proof**2)
        return hashlib.sha256(operation.encode()).hexdigest()

    def validate_hash(self, generated_hash: str):
        length = len(self._puzzle_rule)
        return generated_hash[:length] == self._puzzle_rule


class ValidationUseCase(CryptographicHashUseCase, ProofOfWorkUseCase):
    def validate_chain(self, chain: List[Block]) -> bool:
        previous_block = chain[0]
        index = 1
        while index < len(chain):
            block = chain[index]
            hash_link_is_valid = self._validate_hash_link(
                block, previous_block)
            if hash_link_is_valid is False:
                return False
            proof_of_work_is_valid = self._validate_proof_of_work(
                block, previous_block)
            if proof_of_work_is_valid is False:
                return False
            previous_block = block
            index += 1
        return True

    def _validate_hash_link(self, block: Block, previous_block: Block) -> bool:
        previous_hash = block.previous_hash
        if previous_hash != self.generate_block_hash(previous_block):
            return False
        return True

    def _validate_proof_of_work(self, block: Block,
                                previous_block: Block) -> bool:
        previous_proof = previous_block.proof
        proof = block.proof
        generated_hash = self.generate_proof_hash(proof, previous_proof)
        hash_resolves_puzzle = self.validate_hash(generated_hash)
        if hash_resolves_puzzle is False:
            return False
        return True
