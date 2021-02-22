import time
import requests

cookies = {
    '3N5L_8c5a_saltkey': 'r2qNvpHv',
    '3N5L_8c5a_lastvisit': '1610090087',
    '3N5L_8c5a_pc_size_c': '0',
    '3N5L_8c5a_atarget': '1',
    '3N5L_8c5a_visitedfid': '169',
    '_uab_collina': '161018769145491901291746',
    '3N5L_8c5a_viewid': 'tid_13672',
    '3N5L_8c5a_sid': 'xZ6aAS',
    '3N5L_8c5a_ulastactivity': '0279%2FDUz3mAh4oPFP8jmrsxwgpkhTrO0d5VpfN9%2FHLhKb%2Bemk41O',
    '3N5L_8c5a_auth': 'f9desxvYENfr65XXGSaqEfXssg26P7EQ%2F%2Ff1ISPc44BT5s3L8ts5xuGlEO8CaYd%2B0c0sJozKkhE36kaIEOK1puhS8ME',
    '3N5L_8c5a_lip': '111.173.170.120%2C1581074842',
    '3N5L_8c5a_security_cookiereport': 'b719Qb%2FbYljntl28Rz1cS4zxQ9vHoUDPeDIVu52L%2FsfPdhtGJVAe',
    '3N5L_8c5a_myrepeat_rr': 'R0',
    '3N5L_8c5a_connect_is_bind': '0',
    '3N5L_8c5a_noticeTitle': '1',
    '3N5L_8c5a_smile': '4D1',
    'popnotice': 'hj535546',
    '3N5L_8c5a_st_t': '100402%7C1610093935%7C07ab61b3337bce3425be15395e335b7d',
    '3N5L_8c5a_forum_lastvisit': 'D_169_1610093935',
    '3N5L_8c5a_st_p': '100402%7C1610094066%7Ce5fe43097128b94a4715ee48a4e1ec3f',
    '3N5L_8c5a_sendmail': '1',
    '3N5L_8c5a_lastcheckfeed': '100402%7C1610094105',
    '3N5L_8c5a_lastact': '1610094128%09misc.php%09patch',
}

headers = {
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'iframe',
    'Referer': 'https://bbs.tohkalove.com/gsignin-index.html',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

params = (
    ('action', 'signin'),
    ('formhash', '2990b739'),
)

s = requests.session()
s.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

def get_header(url):
    return s.head(url)


def get_server_time(res):
    server_date = res.headers['Date'][:-4]
    server_timezone = res.headers['Date'][-4:]
    server_timestr = time.strptime(server_date, "%a, %d %b %Y %H:%M:%S")
    server_time = time.strftime("%Y-%m-%d %H:%M:%S", server_timestr)

    return {'server_time':server_time, 'server_timezone':server_timezone, 'server_hour': server_timestr.tm_hour, 'server_min': server_timestr.tm_min}


if __name__=='__main__':
    server_info=get_server_time(get_header('https://bbs.tohkalove.com'))
    '''
    while (server_info['server_hour'] == 11 and server_info['server_min'] >= 50):  # 如果服务器时间大于11：50，那就睡到12：00。
        print(f'当前服务器时间为：{server_info["server_time"]}，服务器时区为：{server_info["server_timezone"]}')
        print('正在睡觉，1分钟后再看')
        time.sleep(60)
        server_info=get_server_time(get_header('https://bbs.tohkalove.com'))
    '''
    print(f'当前服务器时间为：{server_info["server_time"]}，服务器时区为：{server_info["server_timezone"]}')
    print('到点了，上号！！')
    response = requests.get('https://bbs.tohkalove.com/gsignin-index.html', headers=headers, params=params, cookies=cookies)
    print(response.text)
    
    print('程序结束')