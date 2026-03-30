from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from rembg import remove


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['post'],
    allow_headers=['*'],
)


@app.post('/removeBg')
async def removeBG(file:UploadFile=File(...)):
    input_data = await file.read()
    output = remove(input_data)
    return Response(content=output, media_type='image/png')
