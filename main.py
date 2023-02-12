# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from eth_account import Account
import secrets
import hashlib
from web3 import Web3


def get_balance(user_hash):
    # Connect to INFURA HTTP End Point
    infura_url = 'https://avalanche-fuji.infura.io/v3/YOURACCNT'  # your uri
    w3 = Web3(Web3.HTTPProvider(infura_url))
    # Check Connection
    print(w3.isConnected())
    balance = w3.eth.getBalance(user_hash)
    avBalance = w3.fromWei(balance, 'ether')
    print(avBalance)

class Web3Account:

    def generate_address(self, name):
        # Use a breakpoint in the code line below to debug your script.
        print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
        priv = secrets.token_hex(32)
        private_key = "0x" + priv
        print("SAVE BUT DO NOT SHARE THIS:", private_key)
        self.web3Account = Account.from_key(private_key)
        fname = hashlib.sha3_512(str(self.web3Account.address).encode('utf-8'))
        print(str(fname))
        with open(name+str(fname.hexdigest()), 'w') as f:
            f.write(private_key)
        print("Address:",  self.web3Account.address)
        return  self.web3Account.address




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # generate_address('PyCharm')
    Web3Account().generate_address('sam')
    get_balance('0x9c78D2239905C0Db0c9a574A680B9ECD05332125')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
