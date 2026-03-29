from urllib import request
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()
app.mount('/page/static', StaticFiles(directory='page/static'),name='static')

templates = Jinja2Templates(directory='page/templates')

HTML_FILE = Path('page/index.html')

@app.get('/',response_class=HTMLResponse)
async def home():
    return templates.TemplateResponse('index.html',{'request':request,'title':'My Page'})

@app.get('/products')
async def product():
    productsList = ['Iphone','Ipad','Ipod']
    return productsList
class Model(BaseModel):
    identifier:str = 'base'

@app.get('/devices')
async def devices(identifier:str):
    return identifier