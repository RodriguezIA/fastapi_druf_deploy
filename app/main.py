from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.title = "Example deploy on railway"
app.version = "0.0.1"

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/', tags=['home'])
def home():
    return HTMLResponse('<h1>Hello Railway!!!!</h1>')

