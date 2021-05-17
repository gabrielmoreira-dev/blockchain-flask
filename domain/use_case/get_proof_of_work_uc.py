from dataclasses import dataclass
from . import ProofOfWorkUseCase


@dataclass
class GetProofOfWorkUCParams:
    previous_proof: int


class GetProofOfWorkUC(ProofOfWorkUseCase):
    def execute(self, params: GetProofOfWorkUCParams) -> int:
        new_proof = 1
        check_proof = False
        while check_proof is False:
            generated_hash = self.generate_proof_hash(new_proof,
                                                      params.previous_proof)
            hash_resolves_puzzle = self.validate_hash(generated_hash)
            if hash_resolves_puzzle:
                check_proof = True
            else:
                new_proof += 1
        return new_proof