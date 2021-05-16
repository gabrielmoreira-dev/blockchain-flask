from lib.data.repository.blockchain_repository import BlockchainRepository
from lib.data.local.data_source.blockchain_lds import BlockchainLDS

blockchain_lds = BlockchainLDS()
blockchain_repository = BlockchainRepository(blockchain_lds)