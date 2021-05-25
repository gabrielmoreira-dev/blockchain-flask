import requests
from domain.model.blockchain import Blockchain


class BlockchainRDS:
    def get_blockchain(self, address: str):
        response = requests.get(f'http://{address}/chain')
        if response.status_code == 200:
            data = response.json()
            return data
        return None