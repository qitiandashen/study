import json

import requests

base_url='https://api9.ahqyc.com/sysuser/login?login_token='
body={"userName":"admin","password":"QwKj2018"}
headers={'content-type': 'application/json '}
try:
    respones=requests.post(base_url,data=json.dumps(body),headers=headers)
    if respones.status_code==200:

        results=json.loads(respones.text)
        if results['msg']=='success':
            print('登录成功')
        else:
            print('登录失败')
            print(results['msg'])
    else:
        raise Exception('https error info:%s' %respones.status_code)
except Exception as e:
    print(e)

'''print(results)
print(results['msg'])
print(respones.status_code)
print(respones.text)'''