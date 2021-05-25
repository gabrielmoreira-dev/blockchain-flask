import json
from typing import List
from domain.data_repository.blockchain_data_repository import BlockchainDataRepository
from domain.model.block import Block
from domain.model.blockchain import Blockchain
from lib.data.local.data_source.blockchain_lds import BlockchainLDS
from lib.data.mapper.blockchain_remote_to_domain import BlockchainRemoteToDomain
from lib.data.remote.data_source.blockchain_rds import BlockchainRDS


class BlockchainRepository(BlockchainDataRepository):
    def __init__(self, blockchain_lds: BlockchainLDS,
                 blockchain_rds: BlockchainRDS):
        self.blockchain_lds = blockchain_lds
        self.blockchain_rds = blockchain_rds

    def insert_block(self, block: Block):
        self.blockchain_lds.insert_block(block)

    def get_last_index(self) -> int:
        return self.blockchain_lds.get_last_index()

    def get_last_block(self) -> Block:
        return self.blockchain_lds.get_last_block()

    def get_local_blockchain(self) -> Blockchain:
        chain = self.blockchain_lds.get_chain()
        length = len(chain)
        return Blockchain(chain, length)

    def set_local_blockchain(self, chain: List[Block]):
        self.blockchain_lds.set_chain(chain)

    def get_remote_blockchain(self, address: str) -> Blockchain:
        data = self.blockchain_rds.get_blockchain(address)
        return BlockchainRemoteToDomain.toDM(data)