from web3 import Web3

ganache_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))
print(str(web3.isConnected()))
print(web3.eth.block_number)

account_1 = '0x9858cFc1Cc590dD5fb4F181F84B094278701Af16'
account_2 = '0x12aA19CB439bB84c3b56218Ac1A40De85108A533'
private_key = '3ab92931bb218c61f3bc73e959ca7c8ebd98cc60f8ec6c16dfb39405751affc1'

# Get Nonce
nonce = web3.eth.getTransactionCount(account_1)

# Build Transaction
tx = {
    'nonce':nonce,
    'to':account_2,
    'value': web3.toWei(1, 'ether'),
    'gas':2000000,
    'gasPrice':web3.toWei(50, 'gwei')
}

# Sign Transaction
signed_tx = web3.eth.account.sign_transaction(tx, private_key)

# Send Transactions
hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

# Get Transaction Hash
print(web3.toHex(hash))
