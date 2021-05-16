from lib.provider import blockchain_repository, mempool_repository
from domain.use_case.create_block_uc import CreateBlockUC
from domain.use_case.get_hash_uc import GetHashUC
from domain.use_case.get_previous_block_uc import GetPreviousBlockUC
from domain.use_case.get_proof_of_work_uc import GetProofOfWorkUC
from domain.use_case.get_transactions_uc import GetTransactionsUC
from .mineration_controller import MinerationController


class MinerationFactory:
    def makeController():
        create_block_uc = CreateBlockUC(blockchain_repository)
        get_hash_uc = GetHashUC()
        get_previous_block_uc = GetPreviousBlockUC(blockchain_repository)
        get_proof_of_work_uc = GetProofOfWorkUC()
        get_transactions_uc = GetTransactionsUC(mempool_repository)
        return MinerationController(
            get_previous_block_uc=get_previous_block_uc,
            get_proof_of_work_uc=get_proof_of_work_uc,
            get_hash_uc=get_hash_uc,
            create_block_uc=create_block_uc,
            get_transactions_uc=get_transactions_uc)
