from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def main():
    return {'message': 'Hello World'}

@app.get('/products')
async def product():
    productsList = ['Iphone','Ipad','Ipod']
    return productsList
class Model(BaseModel):
    identifier:str = 'base'

@app.get('/devices')
async def devices(identifier:str):
    return identifier