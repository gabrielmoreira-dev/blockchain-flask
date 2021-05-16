from typing import List
from domain.model.block import Block
from domain.model.transaction import Transaction
from domain.use_case.create_block_uc import CreateBlockUC, CreateBlockUCParams
from domain.use_case.get_hash_uc import GetHashUC, GetHashUCParams
from domain.use_case.get_previous_block_uc import GetPreviousBlockUC
from domain.use_case.get_proof_of_work_uc import GetProofOfWorkUC, GetProofOfWorkUCParams
from domain.use_case.get_transactions_uc import GetTransactionsUC
from .mineration_mapper import MinerationMapper


class MinerationController:
    def __init__(self, get_previous_block_uc: GetPreviousBlockUC,
                 get_proof_of_work_uc: GetProofOfWorkUC,
                 get_hash_uc: GetHashUC, create_block_uc: CreateBlockUC,
                 get_transactions_uc: GetTransactionsUC):
        self.get_previous_block_uc = get_previous_block_uc
        self.get_proof_of_work_uc = get_proof_of_work_uc
        self.get_hash_uc = get_hash_uc
        self.create_block_uc = create_block_uc
        self.get_transactions_uc = get_transactions_uc

    def mine_block(self):
        previous_block = self._get_previous_block()
        previous_proof = previous_block.proof
        proof = self._get_proof_of_work(previous_proof)
        previous_hash = self._generate_block_hash(previous_block)
        transactions = self._get_transactions()
        block = self._create_block(proof, previous_hash, transactions)
        return MinerationMapper.toDict(block)

    def _get_previous_block(self):
        return self.get_previous_block_uc.execute()

    def _get_proof_of_work(self, previous_proof: str):
        params = GetProofOfWorkUCParams(previous_proof)
        return self.get_proof_of_work_uc.execute(params)

    def _generate_block_hash(self, block: Block):
        params = GetHashUCParams(block)
        return self.get_hash_uc.execute(params)

    def _get_transactions(self):
        return self.get_transactions_uc.execute()

    def _create_block(self, proof: str, previous_hash: str,
                      transactions: List[Transaction]):
        params = CreateBlockUCParams(proof, previous_hash, transactions)
        return self.create_block_uc.execute(params)