import requests
import json


def calling_page(pages=1, keywords='', offset=0): 
    load_page = True
    page = pages
    start_point = 0
    while load_page:
        search_term = '%20'.join(keywords.split(' '))
        domain = 'https://www.blibli.com'
        url = f'https://www.blibli.com/backend/search/products?sort=&page={page}&start={start_point}&searchTerm={search_term}&intent=true&merchantSearch=true&multiCategory=true&customUrl=&&channelId=web&showFacet=false&userIdentifier=657116261.U.5578713475148559.1690342388&isMobileBCA=false'

        headers= {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'Cache-Control' : 'no-cache'
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
                terjual = '-'            
            except ValueError:                                                            
                terjual = float('.'.join(products[item]['soldRangeCount']['en'][:-1].split(',')))
                terjual = '{:,}'.format(int(terjual * 1000))

            try:
                link = domain+ products[item]['url']
            except KeyError:
                link = '-'


            product ={
                'nama' : product_name,
                'harga' : product_price,
                'harga-sebelum-diskon' : price_before,
                'diskon' : discount,
                'rating' : review,
                'terjual' : terjual,
                'link-produk' : link
            }

            # print(product)
            yield product
        
        current_page = int(data['data']['paging']['page'])
        total_page = int(data['data']['paging']['total_page'])
        print(f"you're in page {current_page} from {total_page}")
        if current_page < total_page:
            next_page = input('tampilkan lebih banyak? (y/n) :')
            if next_page == 'y':
                load_page = True
                # print(page)
                page = page +1
                start_point = start_point+40
            else:
                load_page= False


run = True
while run:
    search_item = input('masukkan barang yang dicari: ')    
    App_bot = calling_page(keywords=search_item)
    item_index =1
    for data in App_bot:
        print(f'({item_index}) {data}')
        item_index = item_index+1


    running_back = input('cari barang yang lain? (y/n): ')
    if running_back== 'y':
        run = True
    else:
        run = False