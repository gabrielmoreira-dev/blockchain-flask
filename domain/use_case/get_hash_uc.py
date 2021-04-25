import json
import hashlib
from .use_case import UseCase

class GetHashUC(UseCase):
    def execute(self, params):
        encoded_block = json.dumps(
            params.block,
            default=lambda o: o.__dict__, 
            sort_keys=True,
        ).encode()
        return hashlib.sha256(encoded_block).hexdigest()

class GetHashUCParams:
    def __init__(self, block):
        self.block = block