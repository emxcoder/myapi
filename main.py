
import io
from fastapi import FastAPI, File, Request, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from rembg import remove, new_session

import datetime
from PIL import Image
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

icon = Image.open('static/assets/favicon.png').tobytes

# Config
app.mount('/static', StaticFiles(directory='static'),name='static')
templates = Jinja2Templates(directory='templates')

os.makedirs('uploads',exist_ok=True)
app.mount('/uploads',StaticFiles(directory='uploads'),name='uploads')


# HTML_FILE = Path('templates/index.html')


@app.get('/')
async def home(request: Request):
    timeToday = datetime.datetime.now().year
    return templates.TemplateResponse(
        request,
        'index.html',

        {
            'name':'EmxCoder',
            'year':timeToday,
            'image':icon
           
        }
    )

@app.get('/about')
async def about(request: Request):
    return templates.TemplateResponse(
        request,
        'about/about.html',
        {'date':datetime.datetime.now().year}
    )

@app.post('/removeBg')
async def removeBGAction(request:Request, file:UploadFile=File(...)):

    session = new_session()
    contents = await file.read()

    input_image = Image.open(io.BytesIO(contents)).convert("RGBA")
    output_image = await remove(input_image,session=session)


    output_path = "uploads/output.png"
    try:
        output_image.save(output_path)
    except:
        print('erro')
    
    

    return templates.TemplateResponse(
        request,
        "remover/removebg.html",
        {
            "image": "/uploads/output.png"
        }
    )


@app.get('/remove')
async def removepage(request: Request):
    return templates.TemplateResponse(
        request,
        'remover/removebg.html',
        {'date':datetime.datetime.now().year}
    )