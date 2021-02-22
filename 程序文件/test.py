import os
import time
import requests
import datetime


PARAM = os.environ['MY_PARAM']
PARAM={'param':PARAM}
RESULT_DIR="执行结果"+os.sep
RESULT_FILE_NAME=RESULT_DIR+datetime.datetime.now().strftime("%Y-%m-%d")+".txt"
if not os.path.exists(RESULT_DIR):
  os.makedirs(RESULT_DIR)


result = requests.get('http://httpbin.org/get',params=PARAM).text
with open(RESULT_FILE_NAME,'w') as f:
  f.write(result+'\n')
print(result)
print('')
print(os.getcwd())
print(os.listdir())
