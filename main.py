from web3 import Web3
import time

# Connect to Ganache
provider = Web3.HTTPProvider("http://localhost:7545")
w3 = Web3(provider)

if not w3.isConnected():
    print("Connection to Ethereum failed")
    exit()
print("Connected to Ethereum node")

# Contract setup
contract_address = Web3.toChecksumAddress("0x2f32f0aB35559095756e32B16c788015C8E125dc")

abi = [
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "internalType": "address", "name": "depositor", "type": "address"},
            {"indexed": False, "internalType": "uint256", "name": "value", "type": "uint256"},
            {"indexed": False, "internalType": "string", "name": "destination", "type": "string"}
        ],
        "name": "EtherDeposited",
        "type": "event"
    }
]

contract = w3.eth.contract(address=contract_address, abi=abi)
log_filter = contract.events.EtherDeposited.createFilter(fromBlock=0)

ledger = {}

print("Watching for EtherDeposited events...")

while True:
    entries = log_filter.get_new_entries()

    for entry in entries:
        depositor = entry["args"]["depositor"]
        eth_value = w3.fromWei(entry["args"]["value"], "ether")
        cosmos_recipient = entry["args"]["destination"]

        print(f"\nDeposit detected on Ethereum:")
        print(f"{depositor} locked {eth_value} ETH for {cosmos_recipient}")

        ledger[cosmos_recipient] = ledger.get(cosmos_recipient, 0) + float(eth_value)
        print(f"Minted {eth_value} cETH on Cosmos for {cosmos_recipient}")
        print(f"Updated balance: {ledger[cosmos_recipient]} cETH")

    time.sleep(1)
