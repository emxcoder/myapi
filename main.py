
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from rembg import remove



app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou teu domínio do vercel
    allow_methods=["*"],
    allow_headers=["*"],
)

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

# @app.post('/remove-bg')
# async def removeBG(file: UploadFile= File(...)):
#     input_data = await file.read()
#     output = remove(input_data)
#     return Response(content=output,media_type='image/png')