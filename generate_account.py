from algosdk.account import generate_account
from dotenv import load_dotenv, set_key

load_dotenv()

pk, address = generate_account()
print(pk, address)

set_key('.env', key_to_set='pk', value_to_set='pk')
set_key('.env', key_to_set='address', value_to_set='address')

#Use Algorand testnet dispenser to have MBR for deploying applications and fees for sending transactions
# https://bank.testnet.algorand.network/
