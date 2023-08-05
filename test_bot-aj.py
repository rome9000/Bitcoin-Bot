import coinbase
from coinbase.wallet.client import Client
from coinbase.wallet.client import OAuthClient


print("hello world")

# Client instatiation and Coinbase information
# To generate API key visit https://help.coinbase.com/en/exchange/managing-my-account/how-to-create-an-api-key
coinbase_API_key = '9xF36UsqaybNxP2M'
coinbase_API_secret = '6NXAzklQF2BwrlQivB0t6alFOmBXuqfW'
client = Client(coinbase_API_key, coinbase_API_secret)
# OAuth made user specific methods work
client = OAuthClient("16da44729b0f8fd1009ed6f20d0ecdb5c16ebdadd763a9c70d74735314ee680d", "16da44729b0f8fd1009ed6f20d0ecdb5c16ebdadd763a9c70d74735314ee680d") 
print(client.get_current_user())





#=====Random statements========#
# accounts = client.get_accounts()
# assert isinstance(accounts.data, list)
# assert accounts[0] is accounts.data[0]
# assert len(accounts[::]) == len(accounts.data)