import json
import hashlib
from .use_case import UseCase

class CryptographicHashUseCase(UseCase):
    def generate_block_hash(self, block):
        encoded_block = json.dumps(
            block,
            default=lambda o: o.__dict__, 
            sort_keys=True,
        ).encode()
        return hashlib.sha256(encoded_block).hexdigest()

