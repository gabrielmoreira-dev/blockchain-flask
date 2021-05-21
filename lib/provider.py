from lib.data.local.data_source.address_lds import AddressLDS
from lib.data.local.data_source.blockchain_lds import BlockchainLDS
from lib.data.local.data_source.mempool_lds import MempoolLDS
from lib.data.local.data_source.network_lds import NetworkLDS
from lib.data.repository.address_repository import AddressRepository
from lib.data.repository.blockchain_repository import BlockchainRepository
from lib.data.repository.mempool_repository import MempoolRepository
from lib.data.repository.network_repository import NetworkRepository

address_lds = AddressLDS()
address_repository = AddressRepository(address_lds)

blockchain_lds = BlockchainLDS()
blockchain_repository = BlockchainRepository(blockchain_lds)

mempool_lds = MempoolLDS()
mempool_repository = MempoolRepository(mempool_lds)

network_lds = NetworkLDS()
network_repository = NetworkRepository(network_lds)