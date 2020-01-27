import  requests
import time

def query(url):
    requests.get(url)

start = time.time()
for i in range(100):
    query('https://www.baidu.com/')

end = time.time()

print(f'单线程循环访问100次百度首页，耗时：{end-start}')

#单线程循环访问100次百度首页，耗时：29.074136972427368