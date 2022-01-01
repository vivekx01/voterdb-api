import json
from web3 import Web3
with open ("./admin/blockchain/Election.json","r") as file:
    election = json.load(file)
    abi = election["abi"]
with open ("./admin/blockchain/contract-address.json") as file:
    addr = json.load(file)
    caddr = addr["electioncontract"]
w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/9b000c2d0d76414d906e15eace34cba5"))
electioncontract = w3.eth.contract(address=caddr, abi=abi)
def getdata():
    count = electioncontract.functions.candidatesCount().call()
    candidatesarray = []
    for i in range(1,count+1):
        data = electioncontract.functions.candidates(i).call()
        candidatesarray.append(data)
    return candidatesarray
def getcount():
    count = electioncontract.functions.candidatesCount().call()
    return count

def getsignerstatus(address):
    status = electioncontract.functions.voters(address).call()
    return status
