import requests

cookies = {
    'autologin_trustie': '4aa262a163d74699bf16830ad611107f2efad2e0',
    '_educoder_session': '06b564a3d652a99cf8af4e7c62eefd2c',
}

headers = {
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'Accept': 'application/json',
    'DNT': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Content-Type': 'application/json; charset=utf-8',
    'Origin': 'https://www.educoder.net',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.educoder.net/users/p6u7nail9/classrooms',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

response = requests.post('https://data.educoder.net/api/users/attendance.json', headers=headers, cookies=cookies)
print(response.text)