import hashlib
from abc import abstractmethod
from .use_case import UseCase

class PoWUseCase(UseCase):
    _puzzle_rule = '0000'

    def generate_hash(self, proof, previous_proof):
        operation = str(proof**2 - previous_proof**2)
        return hashlib.sha256(operation.encode()).hexdigest()

    def verify_hash(self, generated_hash):
        length = len(self._puzzle_rule)
        return generated_hash[:length] == self._puzzle_rule

