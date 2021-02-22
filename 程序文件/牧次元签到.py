import json
import requests


def sign_1():
  headers = {
      'authority': 'www.mucyacg.net',
      'content-length': '0',
      'accept': 'application/json, text/plain, */*',
      'dnt': '1',
      'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3Lm11Y3lhY2cubmV0IiwiaWF0IjoxNjEzODc2MTYwLCJuYmYiOjE2MTM4NzYxNjAsImV4cCI6MTYxNDQ4MDk2MCwiZGF0YSI6eyJ1c2VyIjp7ImlkIjoiODU3NjYifX19.UniWWaYvCyGw7bqHUeRzuyDeU0jqHN2ohwr964kBiF0',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
      'origin': 'https://www.mucyacg.net',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': 'https://www.mucyacg.net/gold/credit',
      'accept-language': 'zh-CN,zh;q=0.9',
      'cookie': 'wordpress_logged_in_aeb7c794e114d723e5cdb9fc2c1da89e=user85766_462%7C1615085760%7CfIVkkPbmFlqsBrCAU8riPyo84C28clpnJAatr1E7lmZ%7C9fb5a708fa497ef4085ede0424d58111b402528e793419e9359b5a2419189263; PHPSESSID=j0qjfugedhlhuf8bg8bq5tgtv8',
  }

  response = requests.post('https://www.mucyacg.net/wp-json/b2/v1/userMission', headers=headers)
  print(response.text)


def sign_2():
  headers = {
      'authority': 'www.mucyacg.net',
      'accept': 'application/json, text/plain, */*',
      'dnt': '1',
      'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3Lm11Y3lhY2cubmV0IiwiaWF0IjoxNjEzOTU0MTIxLCJuYmYiOjE2MTM5NTQxMjEsImV4cCI6MTYxNDU1ODkyMSwiZGF0YSI6eyJ1c2VyIjp7ImlkIjoiODU3NjYifX19.pTMw4xo62hdJzdzacjDUEAB-wRi_6lEJgpqyDJygpCE',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
      'content-type': 'application/x-www-form-urlencoded',
      'origin': 'https://www.mucyacg.net',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': 'https://www.mucyacg.net/gold/credit',
      'accept-language': 'zh-CN,zh;q=0.9',
      'cookie': 'wordpress_logged_in_aeb7c794e114d723e5cdb9fc2c1da89e=user85766_462%7C1615163721%7CkRGKtmQr4ZAHFG1BKxTSkTPWoU5UXw1p3kqb62BsfVj%7Cac3beb16a62728fdd748eceb82c3629a51603908b0ef11857294c28683b6a1a2; PHPSESSID=vn9m4guhdrnllpnatfq85erbq8',
  }

  data = {
    'count': '10',
    'paged': '1'
  }

  response = requests.post('https://www.mucyacg.net/wp-json/b2/v1/getUserMission', headers=headers, data=data)
  print(json.loads(response.text)['mission']['credit'])

if __name__=='__main__':
  sign_2()
  sign_1()