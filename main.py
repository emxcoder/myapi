
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

# Config
app.mount('/static', StaticFiles(directory='static'),name='static')
templates = Jinja2Templates(directory='templates')


# HTML_FILE = Path('templates/index.html')

@app.get('/')
async def home(request: Request):
    return templates.TemplateResponse(
        request,
        'index.html',
        {
            'name':'EmxCoder',
           
        }
    )

@app.get('/products')
async def product():
    productsList = ['Iphone','Ipad','Ipod']
    return productsList
class Model(BaseModel):
    identifier:str = 'base'

@app.get('/devices')
async def devices(identifier:str):
    return identifier