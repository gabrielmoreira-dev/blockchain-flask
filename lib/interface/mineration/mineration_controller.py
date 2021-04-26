from domain.use_case.create_block_uc import CreateBlockUCParams
from domain.use_case.get_hash_uc import GetHashUCParams
from domain.use_case.get_previous_block_uc import GetPreviousBlockUCParams
from domain.use_case.get_proof_of_work_uc import GetProofOfWorkUCParams
from .mineration_mapper import MinerationMapper


class MinerationController:
    def __init__(self, get_previous_block_uc, get_proof_of_work_uc,
                 get_hash_uc, create_block_uc):
        self.get_previous_block_uc = get_previous_block_uc
        self.get_proof_of_work_uc = get_proof_of_work_uc
        self.get_hash_uc = get_hash_uc
        self.create_block_uc = create_block_uc

    def mine_block(self):
        previous_block = self._get_previous_block()
        previous_proof = previous_block.proof
        proof = self._get_proof_of_work(previous_proof)
        previous_hash = self._generate_block_hash(previous_block)
        block = self._create_block(proof, previous_hash)
        return MinerationMapper.toVM(block)

    def _get_previous_block(self):
        params = GetPreviousBlockUCParams()
        return self.get_previous_block_uc.execute(params)

    def _get_proof_of_work(self, previous_proof):
        params = GetProofOfWorkUCParams(previous_proof)
        return self.get_proof_of_work_uc.execute(params)

    def _generate_block_hash(self, block):
        params = GetHashUCParams(block)
        return self.get_hash_uc.execute(params)

    def _create_block(self, proof, previous_hash):
        params = CreateBlockUCParams(proof, previous_hash)
        return self.create_block_uc.execute(params)