from .proof_of_work_use_case import ProofOfWorkUseCase

class GetProofOfWorkUC(ProofOfWorkUseCase):
    def execute(self, params):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            generated_hash = self.generate_hash(new_proof, params.previous_proof)
            hash_resolves_puzzle = self.verify_hash(generated_hash)
            if hash_resolves_puzzle:
                check_proof = True
            else:
                new_proof += 1
        return new_proof

class GetProofOfWorkUCParams:
    def __init__(self, previous_proof):
        self.previous_proof = previous_proof