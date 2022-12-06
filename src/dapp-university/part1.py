from web3 import Web3
infura_ul = 'https://mainnet.infura.io/v3/d601d60a265a4cfdb1986ab31667a855'
web3 = Web3(Web3.HTTPProvider(infura_ul))
print('Are we connected? ' + str(web3.isConnected()))

print('Latest block number: ' + str(web3.eth.block_number))

wallet_address = '0xe2b899D4FF3709a3B947A06575220a91C4BCC769'
ether_amount_wei = web3.eth.get_balance(wallet_address)
ether_amount = web3.fromWei(ether_amount_wei, 'ether')
print('Get balance from my ETH account: ' + str(ether_amount))