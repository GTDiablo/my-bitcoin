from dataclasses import dataclass


@dataclass
class Transaction:
    _id: str
    from_wallet: str
    to_wallet: str
    amount: int
