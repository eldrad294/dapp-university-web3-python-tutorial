from solcx import compile_source, install_solc
install_solc("0.6.0")

compiled_solidity = compile_source(
    """
    // SPDX-License-Identifier: MIT

    pragma solidity ^0.8.12;

    contract HelloWorld {

        string public message;

        constructor() {
            message = "Hello World!";
        }

        function setMessage(string memory _message) public{
            message = _message;
        }

        function getMessage() view public returns (string memory){
            return message;
        }
    }
    """
, output_values=['abi','bin'])

# print(compiled_solidity)

contract_id, contract_interface = compiled_solidity.popitem()
# print(contract_id)
# print(contract_interface)

from web3 import Web3
w3 = Web3(Web3.EthereumTesterProvider())
w3.eth.default_account = w3.eth.accounts[0]
abi = contract_interface['abi']
bytecode = contract_interface['bin']

HelloWorldContract = w3.eth.contract(abi=abi, bytecode=bytecode)
# print(HelloWorldContract)

# tx_hash = HelloWorldContract.constructor().transact()
# tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# print(f"Transaction Receipt {tx_receipt}")

# message = HelloWorldContract.functions.getMessage().call()
# print(message)

# print(HelloWorld.getMessage().transact())
# HelloWorld.setMessage('Hello2!').transact()
# print(HelloWorld.getMessage().transact())
