import requests


def sign():
  headers = {
      'authority': 'cywacg.moe',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
      'dnt': '1',
      'accept': '*/*',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': 'https://cywacg.moe/',
      'accept-language': 'zh-CN,zh;q=0.9',
      'cookie': 'wordpress_sec_cf5c0401222a9989ef8b147c579f86bf=zkaxfXsOq0DTYpyiji6G5TMFwLCdoLlV%7C1612673980%7CRmECY0LEjYV3Fzv5iqeQhiSVPMD8VHvAtrWaLazNz2C%7C6f3924690173844bc415a344ca8765c95dc354768a3a05e587a18bdb00e6a53f; PHPSESSID=nob27jqrog5c34s43c7q5varu9; wordpress_logged_in_cf5c0401222a9989ef8b147c579f86bf=zkaxfXsOq0DTYpyiji6G5TMFwLCdoLlV%7C1612673980%7CRmECY0LEjYV3Fzv5iqeQhiSVPMD8VHvAtrWaLazNz2C%7C08f1868a1e65be362bfc93de65ada08844682753cd3a6ffa11de054e36481281',
  }

  params = (
      ('_nonce', 'afb264cc85'),
      ('action', '7d3f120948b5c969a5fd4ad5b7e73d4b'),
      ('type', 'goSign'),
  )

  response = requests.get('https://cywacg.moe/wp-admin/admin-ajax.php', headers=headers, params=params)
  print(response.text)

def thumbs_up():
  headers = {
      'authority': 'cywacg.moe',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
      'dnt': '1',
      'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryVsSV0KlCVRA3xu8h',
      'accept': '*/*',
      'origin': 'https://cywacg.moe',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': 'https://cywacg.moe/612',
      'accept-language': 'zh-CN,zh;q=0.9',
      'cookie': 'wordpress_sec_cf5c0401222a9989ef8b147c579f86bf=zkaxfXsOq0DTYpyiji6G5TMFwLCdoLlV%7C1612673980%7CRmECY0LEjYV3Fzv5iqeQhiSVPMD8VHvAtrWaLazNz2C%7C6f3924690173844bc415a344ca8765c95dc354768a3a05e587a18bdb00e6a53f; PHPSESSID=nob27jqrog5c34s43c7q5varu9; wordpress_logged_in_cf5c0401222a9989ef8b147c579f86bf=zkaxfXsOq0DTYpyiji6G5TMFwLCdoLlV%7C1612673980%7CRmECY0LEjYV3Fzv5iqeQhiSVPMD8VHvAtrWaLazNz2C%7C08f1868a1e65be362bfc93de65ada08844682753cd3a6ffa11de054e36481281; vpid[612]=1',
  }

  params = (
      ('_nonce', 'afb264cc85'),
      ('action', '99e467b1d85bd59347684b87a4e5901c'),
      ('type', 'add'),
  )

  data = '47864'

  response = requests.post('https://cywacg.moe/wp-admin/admin-ajax.php', headers=headers, params=params, data=data)
  print(response.text)



if __name__=="__main__":
  thumbs_up()