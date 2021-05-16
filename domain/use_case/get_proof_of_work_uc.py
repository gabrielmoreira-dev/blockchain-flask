from . import ProofOfWorkUseCase


class GetProofOfWorkUCParams:
    def __init__(self, previous_proof: str):
        self.previous_proof = previous_proof


class GetProofOfWorkUC(ProofOfWorkUseCase):
    def execute(self, params: GetProofOfWorkUCParams):
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