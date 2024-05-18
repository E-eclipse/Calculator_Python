from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

accounts = w3.eth.accounts

for account in accounts:
    balance = w3.eth.get_balance(account)
    print(f"Аккаунт: {account}, Баланс: {balance}")
