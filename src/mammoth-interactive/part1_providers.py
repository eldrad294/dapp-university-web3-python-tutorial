# Various Providers

# 1) Ethereum Tester Provider
from web3 import Web3, EthereumTesterProvider

w3EthereumTester = Web3(EthereumTesterProvider())
print(f'Is EthereumTester provider connected: {str(w3EthereumTester.isConnected())}')

# 2) Infure Provider
w3Infura = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/d601d60a265a4cfdb1986ab31667a855'))
print(f'Is Infure provider connected: {str(w3EthereumTester.isConnected())}')
