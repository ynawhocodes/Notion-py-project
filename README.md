# Notion-py-project
๐ช API๋ก ๋ฐ์ ๋ฐ์ดํฐ๋ฅผ Notion์ ์๋ ์๋ก๋
 
### 1) Notion database์ ์๋ ์๋ก๋  
![notionTest](https://user-images.githubusercontent.com/48620082/188434140-bb19d917-df93-4ee4-ac5a-fd71f820a68b.gif)
  
- **notion-py**  
https://github.com/jamalex/notion-py
  
### 2) API ํธ์ถ
```python
import requests
import json

def send_api(path, method):
    API_HOST = "https://dummyjson.com"
    url = API_HOST + path
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))
        print("response status %r" % response.status_code)
        print("response text %r" % response.text)
    except Exception as ex:
        print(ex)

datas = send_api('/products', 'GET')
```
- ํ์คํธํ **DummyJSON API**  
https://github.com/Ovi/DummyJSON  

### 3) API ํธ์ถํ์ฌ Notion์ ์๋ ์๋ก๋  
![autoNotion-test](https://user-images.githubusercontent.com/48620082/188434172-8124aa0e-d7da-4ef3-990d-4d8c34441078.gif)
  
 
