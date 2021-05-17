from typing import List
from dataclasses import dataclass
from .transaction import Transaction


@dataclass
class Block:
    index: str
    timestamp: str
    proof: int
    previous_hash: str
    transactions: List[Transaction]
