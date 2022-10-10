from dataclasses import dataclass
from types import List
#
from .transaction import Transaction


@dataclass
class Block:
    transactions: List[Transaction]
    nonce: int
    previous_block_hash: str

    @property
    def hash(self) -> str:
        pass

    def mine(self, no_null: int) -> None:
        self.nonce += 1
