from dataclasses import dataclass
from .block import Block


@dataclass
class Blockchain:
    chain: [Block]
    length: int