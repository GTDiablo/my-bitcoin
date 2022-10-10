from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class Transaction:
    from_wallet: str
    to_wallet: str
    amount: int
    _id: str = field(default_factory=uuid4)

    @property
    def is_valid(self) -> bool:
        return self.from_wallet != self.to_wallet

    @staticmethod
    def create(from_wallet: str, to_wallet: str, amount: int):
        return Transaction(from_wallet=from_wallet, to_wallet=to_wallet, amount=amount)
