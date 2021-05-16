import json
import hashlib
from abc import ABC, abstractmethod


class UseCase(ABC):
    @abstractmethod
    def execute(self, params):
        pass


class CryptographicHashUseCase(UseCase):
    def generate_block_hash(self, block):
        encoded_block = json.dumps(
            block,
            default=lambda o: o.__dict__,
            sort_keys=True,
        ).encode()
        return hashlib.sha256(encoded_block).hexdigest()


class ProofOfWorkUseCase(UseCase):
    _puzzle_rule = '0000'

    def generate_proof_hash(self, proof, previous_proof):
        operation = str(proof**2 - previous_proof**2)
        return hashlib.sha256(operation.encode()).hexdigest()

    def validate_hash(self, generated_hash):
        length = len(self._puzzle_rule)
        return generated_hash[:length] == self._puzzle_rule
