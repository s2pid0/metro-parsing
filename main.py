# from bs4 import BeautifulSoup
# import requests

# url = "https://4lapy.ru/catalog/suhoy-korm-dlya-koshek-bezzernovoy/"
# response = requests.get(url)
# bs = BeautifulSoup(response.text,"lxml")
# temp = bs.find('div', 'b-header__address_pickup_link_value js_favorite_shop_value')
# print(temp.text)

# url = 'https://api-cis.exponea.com/webxp/projects/a1c7f982-1686-11ea-8645-02473a0220cc/bundle'

# # import requests
# data = requests.get(url).json()
# print(data)

import json
import requests

cookies = {
    'metro_api_session': 'EXlPGVX8luuh2JStNHXHW9ZgzMVhXPXotM6SQk1u',
    '_ga_VHKD93V3FV': 'GS1.1.1711815757.2.1.1711820018.59.0.0',
    'tmr_lvid': '987cab293ea9303b41d312edc5eb3b7c',
    'tmr_lvidTS': '1711812299208',
    '_gcl_au': '1.1.1217202258.1703784484',
    '_ym_visorc': 'b',
    '_ym_d': '1711812299',
    '_ym_isad': '1',
    '_ym_uid': '1711812299486385111',
    'uxs_uid': '740bab20-a5a6-11ee-b876-db689cf62a64',
    'mp_5e1c29b29aeb315968bbfeb763b8f699_mixpanel': '%7B%22distinct_id%22%3A%20%22%24device%3A18e8ff6cb3a15c2-007c25fa9c442-26001b51-144000-18e8ff6cb3a15c3%22%2C%22%24device_id%22%3A%20%2218e8ff6cb3a15c2-007c25fa9c442-26001b51-144000-18e8ff6cb3a15c3%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D',
    '_ga': 'GA1.1.1318420898.1711812299',
    '_slfreq': '633ff97b9a3f3b9e90027740%3A633ffa4c90db8d5cf00d7810%3A1711827218%3B64a81e68255733f276099da5%3A64abaf645c1afe216b0a0d38%3A1711827218',
    'directCrm-session': '%7B%22deviceGuid%22%3A%22777b3633-d6e3-496c-840e-7020691d568e%22%7D',
    'mindboxDeviceUUID': '777b3633-d6e3-496c-840e-7020691d568e',
    '_slfs': '1703784479362',
    '_slid': '66082ec8e24d912de9000f7f',
    '_slsession': 'E36BA535-3017-4020-9219-CCCC6FF21B2A',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json',
    'Origin': 'https://online.metro-cc.ru',
    'Content-Length': '1471',
    'Accept-Language': 'ru',
    'Host': 'api.metro-cc.ru',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Referer': 'https://online.metro-cc.ru/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
}

shop_id = "10"
slug = "kofe"
size="400"

data = f'{{"query":"\\n query Query($storeId: Int!, $slug: String!, $attributes:[AttributeFilter], $filters: [FieldFilter], $from: Int!, $size: Int!, $sort: InCategorySort, $in_stock: Boolean, $eshop_order: Boolean, $is_action: Boolean, $price_levels: Boolean) {{\\n category (storeId: $storeId, slug: $slug, inStock: $in_stock, eshopAvailability: $eshop_order, isPromo: $is_action, priceLevels: $price_levels) {{\\n name \\n# treeBranch {{\\n# id\\n# name\\n# slug\\n# children {{\\n# category_type\\n# id\\n# name\\n# slug\\n# children {{\\n# category_type\\n# id\\n# name\\n# slug\\n# children {{\\n# category_type\\n# id\\n# name\\n# slug\\n# children {{\\n# category_type\\n# id\\n# name\\n# slug\\n# }}\\n# }}\\n# }}\\n# }}\\n# }}\\n products(attributeFilters: $attributes, from: $from, size: $size, sort: $sort, fieldFilters: $filters) {{\\n id\\n \\n name\\n  article\\n \\n url\\n manufacturer {{\\n id\\n name\\n }}\\n \\n stocks {{\\n value\\n text\\n eshop_availability\\n prices_per_unit {{\\n old_price\\n price\\n is_promo\\n discount\\n }}\\n }}\\n }}\\n }}\\n }}\\n","variables":{{"storeId":{shop_id},"sort":"default","size":{size},"from":0,"filters":[{{"field":"main_article","value":"0"}}],"attributes":[],"in_stock":true,"eshop_order":false,"allStocks":false,"slug":"{slug}"}}}}'


response = requests.post('https://api.metro-cc.ru/products-api/graph', headers=headers, cookies=cookies, data=data)

with open('metro-moscow-kofe.json', 'w') as file:
    json.dump(response.json(), file, indent=5, ensure_ascii=False)

shop_id = "15"

data = f'{{"query":"\\n query Query($storeId: Int!, $slug: String!, $attributes:[AttributeFilter], $filters: [FieldFilter], $from: Int!, $size: Int!, $sort: InCategorySort, $in_stock: Boolean, $eshop_order: Boolean, $is_action: Boolean, $price_levels: Boolean) {{\\n category (storeId: $storeId, slug: $slug, inStock: $in_stock, eshopAvailability: $eshop_order, isPromo: $is_action, priceLevels: $price_levels) {{\\n name \\n# treeBranch {{\\n# id\\n# name\\n# slug\\n# children {{\\n# category_type\\n# id\\n# name\\n# slug\\n# children {{\\n# category_type\\n# id\\n# name\\n# slug\\n# children {{\\n# category_type\\n# id\\n# name\\n# slug\\n# children {{\\n# category_type\\n# id\\n# name\\n# slug\\n# }}\\n# }}\\n# }}\\n# }}\\n# }}\\n products(attributeFilters: $attributes, from: $from, size: $size, sort: $sort, fieldFilters: $filters) {{\\n id\\n \\n name\\n  article\\n \\n url\\n manufacturer {{\\n id\\n name\\n }}\\n \\n stocks {{\\n value\\n text\\n eshop_availability\\n prices_per_unit {{\\n old_price\\n price\\n is_promo\\n discount\\n }}\\n }}\\n }}\\n }}\\n }}\\n","variables":{{"storeId":{shop_id},"sort":"default","size":{size},"from":0,"filters":[{{"field":"main_article","value":"0"}}],"attributes":[],"in_stock":true,"eshop_order":false,"allStocks":false,"slug":"{slug}"}}}}'

response = requests.post('https://api.metro-cc.ru/products-api/graph', headers=headers, cookies=cookies, data=data)

with open('metro-spb-kofe.json', 'w') as file:
    json.dump(response.json(), file, indent=5, ensure_ascii=False)
