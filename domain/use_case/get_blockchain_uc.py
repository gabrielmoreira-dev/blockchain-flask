from .use_case import UseCase
from domain.model.blockchain import Blockchain

class GetBlockchainUC(UseCase):
    def __init__(self, blockchain_repository):
        self.blockchain_repository = blockchain_repository

    def execute(self, params):
        chain = self.blockchain_repository.get_chain()
        length = len(chain) 
        return Blockchain(chain, length)

class GetPreviousBlockUCParams:
    pass