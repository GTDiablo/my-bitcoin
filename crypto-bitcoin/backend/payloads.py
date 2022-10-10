from pydantic import BaseModel
from types import List
#
from core import Transaction


# TRANSACTIONS
class TransactionListResponse(BaseModel):
    transactions: List[Transaction]


class TransactionDetailResponse(BaseModel):
    transaction: Transaction


class TransactionCreateResponse(BaseModel):
    transaction: Transaction


class TransactionCreateRequest(BaseModel):
    from_wallet: str
    to_wallet: str
    amount: int

# WALLETS


class WalletListResponse(BaseModel):
    pass


class WalletDetailResponse(BaseModel):
    pass


class WalletCreateResponse(BaseModel):
    pass
