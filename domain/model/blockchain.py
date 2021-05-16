from dataclasses import dataclass
from .block import Block
from typing import List


@dataclass
class Blockchain:
    chain: List[Block]
    length: int