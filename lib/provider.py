from lib.data.repository.blockchain_repository import BlockchainRepository
from domain.use_case.create_block_uc import CreateBlockUC, CreateBlockUCParams
from domain.use_case.get_blockchain_uc import GetBlockchainUC, GetBlockchainUCParams
from domain.use_case.get_hash_uc import GetHashUC, GetHashUCParams
from domain.use_case.get_previous_block_uc import GetPreviousBlockUC, GetPreviousBlockUCParams
from domain.use_case.get_proof_of_work_uc import GetProofOfWorkUC, GetProofOfWorkUCParams
from domain.use_case.validate_chain_uc import ValidateChainUC, ValidateChainUCParams

blockchain_repository = BlockchainRepository()

create_block_uc = CreateBlockUC(blockchain_repository)
get_blockchain_uc = GetBlockchainUC(blockchain_repository)
get_hash_uc = GetHashUC()
get_previous_block_uc = GetPreviousBlockUC(blockchain_repository)
get_proof_of_work_uc = GetProofOfWorkUC()
validate_chain_uc = ValidateChainUC(blockchain_repository)