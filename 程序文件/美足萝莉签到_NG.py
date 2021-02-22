import requests

headers = {
    'authority': 'www.meizuloli.net',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'dnt': '1',
    'x-requested-with': 'XMLHttpRequest',
    'x-wp-nonce': 'fe9aeba2ed',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.meizuloli.net',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.meizuloli.net/archives/8928/comment-page-1',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'wordpress_sec_832d86e31032941ae5a7bc61bbf583b8=First_Y%7C1612927414%7CDAgw0Z4OcpaM3RV5WJ82lgg6aWkEie9pqcrAJgedbZu%7C6b65acf44b64b6db36dba672db6415c8706d9c9909d7d2d68b0e3f87d4f89a3a; __51cke__=; night=0; 8928viewed=1; wordpress_logged_in_832d86e31032941ae5a7bc61bbf583b8=First_Y%7C1612927414%7CDAgw0Z4OcpaM3RV5WJ82lgg6aWkEie9pqcrAJgedbZu%7C96e48fde47c41d8c56aedc94dfcc1b06644895bdd83a809a5b9acfbdb8cc3dd3; current_user_email=1725338233%40qq.com; bigfa_ding_8928=8928; __tins__20941991=%7B%22sid%22%3A%201611717154313%2C%20%22vd%22%3A%203%2C%20%22expires%22%3A%201611719693661%7D; __51laig__=3',
}

data = {
  'sign': '1',
  'ticket': '',
  'randstr': ''
}

response = requests.post('https://www.meizuloli.net/wp-content/plugins/tk-shop/inc/plugins/sign/action/sign.php', headers=headers, data=data)
print(response.text)