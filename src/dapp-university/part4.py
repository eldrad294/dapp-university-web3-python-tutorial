from web3 import Web3
import json

address = Web3.toChecksumAddress('0xd8fBaFA9b5737385b9875eDbdF0392Fe7404ba12')
contract_build = json.loads(open('build/contracts/HelloWorld.json').read().replace('\n',''))
abi = contract_build['abi']

ganache_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))
web3.eth.default_account = web3.eth.accounts[0]
contract = web3.eth.contract(
    address=address, 
    abi=abi
)

# 1) Read from contract (Constructor)
print(contract.functions.getGreeting().call())

# 2) Write to contract
tx_hash = contract.functions.setGreeting("HELLO WORLD, THE SECOND").transact()
web3.eth.wait_for_transaction_receipt(tx_hash)
print(tx_hash)
print(f'Updated greeting {contract.functions.getGreeting().call()}')