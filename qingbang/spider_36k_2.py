import requests
import json
from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://36kr.com/search/articles/%E5%B7%A5%E5%95%86%E8%B4%A2%E7%A8%8E?page=1&ts=1553149021689')
title=driver.title
page=driver.page_source
print(page)
print(title)
'''def get_get_page(url,header):
    try:
        response=requests.get(url,header)
        print(response.status_code)
        if response==200:
            return response.text
        return None
    except Exception as e:
        print('请求错误')
def main():
    header={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36"}
    url="https://36kr.com/search/articles/%E5%B7%A5%E5%95%86%E8%B4%A2%E7%A8%8E?page=1&ts=1553140485745"
    html=get_get_page(url,header)
    print(html)
if __name__=="__main__":
    main()'''