import os
import time
import datetime
import feedparser


RESULT_DIR="执行结果"+os.sep # 执行结果保存到当前目录下的 执行结果/日期.txt 文档里
today=datetime.datetime.now().strftime("%Y-%m-%d")
RESULT_FILE_NAME=RESULT_DIR+today+" JOJODL更新.txt"
if not os.path.exists(RESULT_DIR):
  os.makedirs(RESULT_DIR)


# 网站RSS解析
jojodl=feedparser.parse('https://jojodl.com/feed/')
# 整理为JSON数组
result = ['文件标题：' + entry['title']+'\n来源链接：' + entry['link']+'\n发布时间：' + entry['published'] + '\n下载链接：' + entry['summary'][:entry['summary'].index('|')-1]+'\n文件大小：' + entry['summary'][entry['summary'].index('|')+2:]+'\n\n' for entry in jojodl['entries']]
# pprint.pprint(result[0])
result=''.join(result)
with open(RESULT_FILE_NAME,'w') as f:
  f.write(result)
print(today+' 程序结束！')