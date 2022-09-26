from fake_useragent import UserAgent   # 下载：pip install fake-useragent
import requests

ua = UserAgent()        # 实例化，需要联网但是网站不太稳定-可能耗时会长一些
print(ua.random)  # 随机产生
headers = {
    'User-Agent': ua.random    # 伪装
    }

# 请求
if __name__ == '__main__':
    url = 'https://www.baidu.com/'
    response = requests.get(url, headers=headers ,proxies={"http":"117.136.27.43"})
    print(response.status_code)


