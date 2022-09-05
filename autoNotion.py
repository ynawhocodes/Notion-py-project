from notion.client import NotionClient
from notion.block import * 
from notion.collection import * 
from datetime import datetime 
import notion
import requests
import json

_MY_TOKEN = "04ab146d0f5f1f5b5c7e62ba987c4feb4637d2a39e7e33...9dcc21b1f297e8b73289cf26745a6df7eae043af209689275ce9cc71d77649d896e55f"
_PAGE_URL = "https://www.notion.so/..."

def send_api(path, method):
    API_HOST = "https://dummyjson.com"
    url = API_HOST + path
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))
        # print("response status %r" % response.status_code)
        # print("response text %r" % response.text)
        return response.text
    except Exception as ex:
        print(ex)

def get_collection_schema():
    return {
        "id" : {"name" : "title", "type" : "number"},
        "title" : {"name" : "title", "type" : "text"},
        "description" : {"name" : "description", "type" : "text"},
        "price" : {"name" : "price" , "type" : "number"},
        "discountPercentage" : {"name" : "discountPercentage", "type" : "number"},
        "rating" : {"rating" : "keyword", "type" : "number"}
    }

stringDatas = send_api('/products', 'GET')
datas = json.loads(stringDatas)

client = NotionClient(token_v2=_MY_TOKEN)
page = client.get_block(_PAGE_URL)
Block = page.children[0] 

for data in datas['products']:
    row = Block.collection.add_row() 
    row.id = data['id']
    row.title = data['title']
    row.description = data['description']
    row.price = data['price']
    row.discountPercentage = data['discountPercentage']
    row.rating = data['rating']