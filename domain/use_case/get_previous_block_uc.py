from . import UseCase


class GetPreviousBlockUC(UseCase):
    def __init__(self, blockchain_repository):
        self.blockchain_repository = blockchain_repository

    def execute(self, params):
        return self.blockchain_repository.get_last_block()


class GetPreviousBlockUCParams:
    pass