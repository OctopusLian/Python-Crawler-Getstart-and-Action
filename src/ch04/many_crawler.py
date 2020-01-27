import  requests
import time
from multiprocessing.dummy import Pool

def query(url):
    requests.get(url)

start = time.time()

url_list = []
for i in range(100):
    url_list.append('https://www.baidu.com/')

pool = Pool(5)
pool.map(query,url_list)
end = time.time()
print(f'5线程循环访问100次百度首页，耗时：{end-start}')

#5线程循环访问100次百度首页，耗时：6.339653968811035

