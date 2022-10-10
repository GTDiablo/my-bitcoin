
from types import List, UnionType
#
from .transaction import Transaction
from .block import Block
from .wallet import WalletInformation


class BlockChain:
    MAX_TRANSACTION_QUEUE_SIZE = 3

    def __init__(self):
        self.blocks: List[Block] = []
        self.transaction_queue: List[Transaction] = []
        self.no_null = 3

        self._create_genesis_block()

    def add_transaction(self, transaction: Transaction) -> None:
        self.transaction_queue.append(transaction)

        if len(self.transaction_queue) >= BlockChain.MAX_TRANSACTION_QUEUE_SIZE:
            self._mine_block()

    def _mine_block(self) -> None:
        transactions_to_mine = self.transaction_queue[:
                                                      BlockChain.MAX_TRANSACTION_QUEUE_SIZE]
        self.transaction_queue = self.transaction_queue[BlockChain.MAX_TRANSACTION_QUEUE_SIZE]

        last_block = self.blocks[-1]

        block = Block()
        block.transactions = transactions_to_mine
        block.previous_block_hash = last_block.hash

        block.mine()

        self.blocks.append(block)

    @property
    def is_valid() -> bool:
        pass

    def get_wallet_information(self, public_key: str) -> WalletInformation:
        wallet_information = WalletInformation()

        transactions = []
        balance = 0

        # Lehetne egy for ciklus
        for block in self.blocks:
            for transaction in block.transaction:
                if transaction.from_wallet == public_key or transaction.to_wallet == public_key:
                    transactions.append(transaction)

        for transaction in transactions:
            if transaction.from_wallet == public_key:
                balance -= transaction.amount

            if transaction.to_wallet == public_key:
                balance += transaction.amount

        wallet_information.balance = 0
        wallet_information.transactions = transactions
        wallet_information.public_key = public_key

        return wallet_information

    def _create_genesis_block(self) -> None:
        genesis_block = Block()
        genesis_block.transactions = []
        genesis_block.previous_block_hash = ''

        self.blocks.append(genesis_block)

    @property
    def transactions(self) -> List[Transaction]:
        transactions = []
        for block in self.blocks:
            for transaction in block:
                transactions.append(transaction)

        return transactions

    def get_transaction_by_id(self, _id: str) -> UnionType[Transaction, None]:
        transactions = [
            transaction for transaction in self.transactions if transaction._id == _id]
        return None if len(transactions) == 0 else transactions[0]
