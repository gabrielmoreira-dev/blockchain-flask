from lib.provider import address_repository, blockchain_repository, mempool_repository
from domain.use_case.add_transaction_uc import AddTransactionUC
from domain.use_case.create_block_uc import CreateBlockUC
from domain.use_case.get_hash_uc import GetHashUC
from domain.use_case.get_address_uc import GetAddressUC
from domain.use_case.get_previous_block_uc import GetPreviousBlockUC
from domain.use_case.get_proof_of_work_uc import GetProofOfWorkUC
from .mineration_controller import MinerationController


class MinerationFactory:
    def makeController() -> MinerationController:
        add_transaction_uc = AddTransactionUC(mempool_repository)
        create_block_uc = CreateBlockUC(blockchain_repository,
                                        mempool_repository)
        get_hash_uc = GetHashUC()
        get_previous_block_uc = GetPreviousBlockUC(blockchain_repository)
        get_proof_of_work_uc = GetProofOfWorkUC()
        get_address_uc = GetAddressUC(address_repository)
        return MinerationController(
            add_transaction_uc=add_transaction_uc,
            get_address_uc=get_address_uc,
            get_previous_block_uc=get_previous_block_uc,
            get_proof_of_work_uc=get_proof_of_work_uc,
            get_hash_uc=get_hash_uc,
            create_block_uc=create_block_uc)
