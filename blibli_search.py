import requests
import json

domain = 'https://www.blibli.com'
url = 'https://www.blibli.com/backend/search/products?sort=&page=2&start=40&searchTerm=acer%20predator&intent=true&merchantSearch=true&multiCategory=true&customUrl=&&channelId=web&showFacet=false&userIdentifier=657116261.U.5578713475148559.1690342388&isMobileBCA=false'

headers= {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

r = requests.session()
response = r.get(url=url, headers= headers)
data = json.loads(response.text)
products = data['data']['products']

for item in range(len(products)):
    try:
        product_name  = products[item]['name']
    except KeyError:
        product_name ='-'

    try:        
        product_price = '{:,}'.format(int(''.join(products[item]['price']['priceDisplay'][2:].split('.'))))
    except KeyError:
        product_price = '-'

    try:
        discount = str(products[item]['price']['discount']) + '%'
    except KeyError:
        discount ='-'

    try:
        price_before = '{:,}'.format(int(''.join(products[item]['price']['strikeThroughPriceDisplay'][2:].split('.'))))
    except KeyError:
        price_before = '-'

    try:
        review = float(products[item]['review']['absoluteRating'])
    except KeyError:
        review = '-'

    try:
        terjual = int(products[item]['soldRangeCount']['en'])
    except KeyError:
        terjual ='-'

    try:
        link = domain+ products[item]['url']
    except KeyError:
        link ='-'

    product ={
        'nama' : product_name,
        'harga' : product_price,
        'harga-sebelum-diskon' : price_before,
        'diskon' : discount,
        'rating' : review,
        'terjual' : terjual,
        'link-produk' : link
    }

    print(f'({item+1}) {product}')