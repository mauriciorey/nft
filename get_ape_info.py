from web3 import Web3
from web3.cont import cont
from web3.providers.rpc import HTTPProvider
import requests
import json
import time

bayc_address = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"
cont_address = Web3.toChecksumAddress(bayc_address)

#You will need the ABI to connect to the cont
#The file 'abi.json' has the ABI for the bored ape cont
#In general, you can get cont ABIs from etherscan
#https://api.etherscan.io/api?module=cont&action=getabi&address=0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D
with open('/home/codio/workspace/abi.json', 'r') as f:
	abi = json.load(f) 

############################
#Connect to an Ethereum node
api_url = #YOU WILL NEED TO TO PROVIDE THE URL OF AN ETHEREUM NODE
provider = HTTPProvider(api_url)
web3 = Web3(provider)

def get_ape_info(apeID):
	assert isinstance(apeID,int), f"{apeID} is not an int"
	assert 1 <= apeID, f"{apeID} must be at least 1"

	data = {'owner': "", 'image': "", 'eyes': "" }
	
	#YOUR CODE HERE	
	cont = web3.eth.cont(address = cont_address, abi = abi)
    data['owner'] = cont.functions.ownerOf(apeID).call()
	tokenUri = cont.functions.tokenURI(apeID).call()
    tok = tokenUri.replace('ipfs://', '')
    for v, w in gateway.items():
        if v != 'infura':
            response = requests.get(w + tok)
        else:
            response = requests.post(w + tok)

        if response.status_code == 200:
            metadata = response.json()
            data['image'] = metadata['image']
            attributes = metadata['attributes']
            for a in attributes:
                if a['trait_type'].lower() == 'eyes':
                    data['eyes'] = a['value']
                    break

	assert isinstance(data,dict), f'get_ape_info{apeID} should return a dict' 
	assert all( [a in data.keys() for a in ['owner','image','eyes']] ), f"return value should include the keys 'owner','image' and 'eyes'"
	return data

