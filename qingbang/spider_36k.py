import requests
from urllib.parse import urlencode
def get_index_page(page,keyword):
    data={
        "page": page,
        "per_page": "40",
        "keyword": keyword,
        "entity_type":"post",
        "sort": "date",
        "_": "1552967347865"
    }
    header={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36"

    }
    try:
        url='https://36kr.com/api/search/entity-search?'+urlencode(data)
        response=requests.get(url,header=header)
        if response.status_code==200:
            return response.text
        return None
    except Exception as e:
        print(e)
        return None
def main():
    html=get_index_page(1,'工商财税')
    print(html)
if __name__=='__main__':
    main()
