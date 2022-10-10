from fastapi import FastAPI
#
from core import Transaction, BlockChain, generate_wallet
from .payloads import TransactionCreateRequest, TransactionCreateResponse

block_chain = BlockChain()
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/transactions')
async def list_transactions():
    transactions = block_chain.transactions
    return {"transactions": []}


@app.get('/transactions/{transaction_id}')
async def get_transaction(transaction_id: str):
    transaction = block_chain.get_wallet_information(transaction_id)
    return {"transactions": []}


@app.post('/transactions', response_model=TransactionCreateResponse)
async def create_transaction(transaction_data: TransactionCreateRequest):
    transaction = Transaction.create(
        transaction_data.from_wallet,
        transaction_data.to_wallet,
        transaction_data.amount
    )

    block_chain.add_transaction(transaction)

    return {
        "transaction": {
            "id": transaction._id,
            "from_wallet": transaction.from_wallet,
            "to_wallet": transaction.to_wallet,
            "amount": transaction.amount
        }
    }


@app.get('/wallets')
async def list_wallets():
    return {"wallets": []}


@app.get('/wallets/{public_key}')
async def get_wallet(public_key: str):
    wallet_information = block_chain.get_wallet_information(public_key)
    return {"wallet": []}


@app.post('/wallets')
async def create_wallet():
    wallet = generate_wallet()
    return {"wallet": ""}
