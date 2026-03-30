
from fastapi import FastAPI, Request, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from rembg import remove
from fastapi.responses import Response
import datetime
import os
os.environ["RMBG_NO_GPU"] = "1"


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)


# Config
app.mount('/static', StaticFiles(directory='static'),name='static')
templates = Jinja2Templates(directory='templates')


# HTML_FILE = Path('templates/index.html')


@app.get('/')
async def home(request: Request):
    timeToday = datetime.datetime.now().year
    return templates.TemplateResponse(
        request,
        'index.html',
        {
            'name':'EmxCoder',
            'year':timeToday
           
        }
    )


@app.post('/removeBg')
async def removeBG(file:UploadFile=File(...)):
    input_data = await file.read()
    output = remove(input_data)
    return Response(content=output, media_type='image/png')