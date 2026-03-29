from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from pathlib import Path

app = FastAPI()

HTML_FILE = Path('page/index.html')

@app.get('/',response_class=HTMLResponse)
def home():
    return HTML_FILE.read_text(encoding='utf-8')

@app.get('/products')
async def product():
    productsList = ['Iphone','Ipad','Ipod']
    return productsList
class Model(BaseModel):
    identifier:str = 'base'

@app.get('/devices')
async def devices(identifier:str):
    return identifier