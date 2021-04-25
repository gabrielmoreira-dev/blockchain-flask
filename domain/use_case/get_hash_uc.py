from .cryptographic_hash_use_case import CryptographicHashUseCase

class GetHashUC(CryptographicHashUseCase):
    def execute(self, params):
        return self.generate_block_hash()

class GetHashUCParams:
    def __init__(self, block):
        self.block = block