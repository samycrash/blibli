import requests
import json

url = 'https://www.blibli.com/backend/search/products?sort=&page=2&start=40&searchTerm=acer%20predator&intent=true&merchantSearch=true&multiCategory=true&customUrl=&&channelId=web&showFacet=false&userIdentifier=657116261.U.5578713475148559.1690342388&isMobileBCA=false'

headers= {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

r = requests.session()
response = r.get(url=url, headers= headers)
data = json.loads(response.text)
products = data['data']['products']

for item in range(len(products)):
    product_name  = products[item]['name']

    print(f'({item+1}) {product_name}')