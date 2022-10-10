from dataclasses import dataclass
from types import List
#
from .transaction import Transaction


@dataclass
class Block:
    transactions: List[Transaction]
    previous_block_hash: str
    nonce: int = 0

    @property
    def hash(self) -> str:
        pass

    def mine(self, no_null: int) -> None:
        is_valid = self.hash[:no_null] == '0' * no_null
        while not is_valid:
            self.nonce += 1
