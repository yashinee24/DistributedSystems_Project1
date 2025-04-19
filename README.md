# EthCos: Ethereum to Cosmos Token Transfer Bridge

This project demonstrates a simple cross-chain interaction mechanism between the Ethereum and Cosmos ecosystems. Users on Ethereum can lock ETH and specify a Cosmos destination address, which is then used to mint an equivalent token balance on the Cosmos side.


## Overview

- **Ethereum Side:** A smart contract (`EthCos.sol`) deployed locally via Ganache accepts ETH deposits and logs them using the `EtherDeposited` event.
- **Cosmos Side (Simulated):** A Python script (`main.py`) listens for `EtherDeposited` events and updates a local ledger to reflect token balances on Cosmos.

## Components

### 1. Smart Contract (`EthCos.sol`)
- Accepts ETH and a string representing a Cosmos address.
- Emits an `EtherDeposited` event containing the sender, amount, and destination address.
- Allows users to query their locked ETH via `checkDeposit`.

### 2. Listener Script (`main.py`)
- Built with Web3.py and Python 3.10+.
- Connects to Ganache at `http://localhost:7545`.
- Filters the Ethereum blockchain for `EtherDeposited` events.
- When an event is received, it logs and tracks the corresponding token "mint" on Cosmos.
