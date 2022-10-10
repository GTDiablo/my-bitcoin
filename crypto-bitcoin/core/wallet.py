from dataclasses import dataclass
from typing import List
#
from .transaction import Transaction


@dataclass
class Wallet:
    public_key: str
    private_key: str


@dataclass
class WalletInformation:
    public_key: str
    balance: int
    transactions: List[Transaction]


def generate_wallet() -> Wallet:
    wallet = Wallet()
    wallet.public_key = ''
    wallet.private_key = ''

    return wallet
