from dataclasses import dataclass
from . import CryptographicHashUseCase
from domain.model.block import Block


@dataclass
class GetHashUCParams:
    block: Block


class GetHashUC(CryptographicHashUseCase):
    def execute(self, params: GetHashUCParams):
        return self.generate_block_hash(params.block)