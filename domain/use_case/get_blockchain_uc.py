from .use_case import UseCase

class GetBlockchainUC(UseCase):
    def __init__(self, blockchain_repository):
        self.blockchain_repository = blockchain_repository

    def execute(self, params):
        return self.blockchain_repository.get_blockchain()

class GetPreviousBlockUCParams:
    pass