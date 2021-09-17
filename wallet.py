# Import dependencies
import subprocess
import json
from dotenv import load_dotenv
from constants import *
import os
from pprint import pprint 
# Load and set environment variables
load_dotenv()
mnemonic=os.getenv("mnemonic.env")

# BTC = 'btc'
# ETH = 'eth'
# BTCTEST = 'btc-test'

# Import constants.py and necessary functions from bit and web3
# YOUR CODE HERE
 
 
# Create a function called `derive_wallets`
def derive_wallets(coin): # coin can be either btc, eth, btc-test
    command = f'./derive --mnemonic="{mnemonic}" --coin={coin} --numderive=3 --format=json -g'
    # './derive --mnemonic="cave resource emerge almost cycle erupt sick client price game second enhance" --coin=BTC --numderive=3 --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    # return coin
    return json.loads(output)
    

# Create a dictionary object called coins to store the output from `derive_wallets`.
# coins={key1:value1, 
#        key2: value2}
coins={'btc-test': derive_wallets(BTCTEST), # dervie_wallets('btc-test')
#     {'btc-test': 'BTCTEST', 
       'eth': derive_wallets(ETH)} # dervie_wallets('eth')

pprint(coins)

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin, privkey):# YOUR CODE HERE):
    # You will need to check the coin type, then return one of the following functions based on the library:

    # For ETH, return Account.privateKeyToAccount(priv_key)
    # This function returns an account object from the private key string. You can read more about this object here.
    # For BTCTEST, return PrivateKeyTestnet(priv_key)
    # This is a function from the bit libarary that converts the private key string into a WIF (Wallet Import Format) object. WIF is a special format bitcoin uses to designate the types of keys it generates.
    # You can read more about this function here.
    if coin=ETH: 
        return Account.privateKeyToAccount(privkey)
    if coin=BTCTEST: 
        return PrivateKeyTestnet(privkey)

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(coin, account, to, amount):
    if coin = ETH:
        an_object={'to': to,
                   'from': account, 
                   'value': amount, 
                   'gas': , 
                   'gasPrice': , 
                   'nonce': , 
                   'chainID': }
        return an_object
    # YOUR CODE HERE):
    # YOUR CODE HERE
    return None

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx():# YOUR CODE HERE):
    # YOUR CODE HERE
    return None

