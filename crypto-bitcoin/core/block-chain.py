
from types import List
#
from .transaction import Transaction
from .block import Block


class BlockChain:
    MAX_TRANSACTION_QUEUE_SIZE = 3

    def __init__(self):
        self.block: List[Block] = []
        self.transaction_queue: List[Transaction] = []
        self.no_null = 3

    def add_transaction(self, transaction: Transaction) -> None:
        self.transaction_queue.append(transaction)

        if len(self.transaction_queue) >= BlockChain.MAX_TRANSACTION_QUEUE_SIZE:
            self._mine_block()

    def _mine_block(self) -> None:
        transactions_to_mine = self.transaction_queue[:
                                                      BlockChain.MAX_TRANSACTION_QUEUE_SIZE]
        self.transaction_queue = self.transaction_queue[BlockChain.MAX_TRANSACTION_QUEUE_SIZE]

        block = Block()
        block.transactions = transactions_to_mine

    @property
    def is_valid() -> bool:
        pass

    def get_wallet_information(public_key: str):
        pass
