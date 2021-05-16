from . import CryptographicHashUseCase
from domain.model.block import Block


class GetHashUCParams:
    def __init__(self, block: Block):
        self.block = block


class GetHashUC(CryptographicHashUseCase):
    def execute(self, params: GetHashUCParams):
        return self.generate_block_hash(params.block)