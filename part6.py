from web3 import Web3
infura_url = 'https://mainnet.infura.io/v3/d601d60a265a4cfdb1986ab31667a855'
web3 = Web3(Web3.HTTPProvider(infura_url))

latest_block_number = web3.eth.block_number
# print(latest_block_number)

# print(web3.eth.getBlock(latest_block_number))

# for i in range(0, 10):
#     print(web3.eth.getBlock(latest_block_number - i))

block_hash = '0xd62e67c82572446f76626f30ca2f71535bf0142aeb3d3c418eb5e59da311a870'
print(web3.eth.getTransactionByBlock(block_hash, 2))