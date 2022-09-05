from notion.client import NotionClient
from notion.block import * 
from notion.collection import * 
from datetime import datetime 
import notion

_MY_TOKEN = "04ab146d0f5f1f5b5c7e62ba987c4feb4637d2a39e7e33...9dcc21b1f297e8b73289cf26745a6df7eae043af209689275ce9cc71d77649d896e55f"
_PAGE_URL = "https://www.notion.so/..."

client = NotionClient(token_v2=_MY_TOKEN)
page = client.get_block(_PAGE_URL)

Block = page.children[0] 

row = Block.collection.add_row() 
row.question = '문의 1'
row.date = date(2022, 9, 5)