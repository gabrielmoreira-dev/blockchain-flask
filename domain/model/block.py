from dataclasses import dataclass


@dataclass
class Block:
    index: str
    timestamp: str
    proof: str
    previous_hash: str
