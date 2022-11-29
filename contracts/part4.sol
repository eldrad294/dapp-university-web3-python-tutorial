pragma solidity ^0.8.17;

contract HelloWorld{

    string public greeting;

    constructor() public{
        greeting = "Hello World!";
    }

    function setGreeting(string memory _greeting) public{
        greeting = _greeting;
    }

    function getGreeting() public view returns(string memory){
        return greeting;
    }
}