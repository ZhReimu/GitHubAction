import os
import json
import requests
import datetime


RESULT_DIR="执行结果"+os.sep+"Pixiv"+os.sep 
# 执行结果保存到当前目录下的 执行结果/Pixiv 里
s = requests.session()
s.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "Referer":'https://pixiv.net'
}
api = "https://pix.ipv4.host/ranks"

def init():
    """初始化保存文件夹
    
    """
    if not os.path.exists(RESULT_DIR):
      os.makedirs(RESULT_DIR)

def getdate()->str:
    """获取前两天的日期
    
    """
    date = datetime.date.today() + datetime.timedelta(-2)
    return str(date)

def get_img_urls()->list:
    """获取图片链接
    
    """
    data = {
        'page': '1',
        'date': getdate(),
        'mode': 'day',
        'pageSize': '100'
    }
    res = s.get(api, params=data)
    if res.status_code!=200:
        raise ValueError('请求图片信息出错，错误代码：'+str(res.status_code))
    json_str = res.text
    datas = json.loads(json_str)['data']
    img_urls = []
    pids = []
    for data in datas:
        pids.append(data['id'])
        for img in data['imageUrls']:
            img_urls.append(img['original'])
    if len(pids)>1 and len(img_urls)>1:
        print('本次一共获取了',len(pids),'个作品',len(img_urls),'张图片！')
        return img_urls


def download_img(url):
    """下载图片
    
    """
    filename = url[url.rindex('/')+1:]
    RESULT_FILE_NAME = RESULT_DIR+filename
    if os.exists(RESULT_FILE_NAME):
      print('文件已存在，跳过下载！',filename)
      return "Pass"
    print('开始下载',filename)
    with open(RESULT_FILE_NAME,'wb')as file:
        res = s.get(url)
        if res.status_code!=200:
            raise ValueError('下载图片出错，错误代码：'+str(res.status_code))
        file.write(res.content)
    print('下载完成！\n')


if __name__ == '__main__':
    init()
    urls = get_img_urls()
    for url in urls:
        download_img(url)
        
    print('程序结束！')
    