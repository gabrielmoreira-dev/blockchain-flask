from typing import List
import dataclasses
from domain.model.block import Block


class ConsensusMapper:
    def toDict(chain: List[Block], is_replaced: bool):
        replaced_message = 'The chain was replaced by the largest one'
        not_replaced_message = 'The chain is already the largest one'
        message = replaced_message if is_replaced else not_replaced_message
        blockchain = ConsensusMapper._get_chain(chain)
        return {'message': message, 'chain': blockchain}

    def _get_chain(chain: List[Block]):
        blockchain = []
        for block in chain:
            blockchain.append(dataclasses.asdict(block))
        return blockchain