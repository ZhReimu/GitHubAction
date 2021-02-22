import requests

headers = {
    'authority': 'www.gtloli.one',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'dnt': '1',
    'x-requested-with': 'XMLHttpRequest',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.gtloli.one/forum.php',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'Uusp_2132_saltkey=Mbac9Tcr; Uusp_2132_lastvisit=1610422745; Uusp_2132_atarget=1; Uusp_2132_visitedfid=182D175D84; Uusp_2132_nciaer_topbanner=1; Uusp_2132_seccode=17502.f47592b5113c14da90; Uusp_2132_ulastactivity=1611717264%7C0; Uusp_2132_auth=2b51njdBb6tWTbI6TXL%2BYpheAxFMx%2FbCjSXTBcufIDSasDcnv3%2Be1e8ERQMbYjK4ERQkra%2F4BYVBV9bHlIk%2FJtl3iac; Uusp_2132_nofavfid=1; Uusp_2132_sendmail=1; Uusp_2132_lastact=1611717269%09home.php%09spacecp',
}

params = (
    ('id', 'k_misign:sign'),
    ('operation', 'qiandao'),
    ('format', 'button'),
    ('formhash', '38313513'),
    ('inajax', '1'),
    ('ajaxtarget', 'midaben_sign'),
)

response = requests.get('https://www.gtloli.one/plugin.php', headers=headers, params=params)
print(response.text)
