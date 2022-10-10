from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/transactions')
async def list_transactions():
    return {"transactions": []}


@app.get('/transactions/{transaction_id}')
async def get_transaction():
    return {"transactions": []}


@app.post('/transactions')
async def create_transaction():
    return {"transactions": []}


@app.get('/wallets')
async def list_wallets():
    return {"wallets": []}


@app.get('/wallets/{public_key}')
async def get_wallet():
    return {"wallet": []}


@app.post('/wallet')
async def create_wallet():
    return {"wallet": ""}
