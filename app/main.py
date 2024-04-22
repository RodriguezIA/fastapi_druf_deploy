from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "Example deploy on railway"
app.version = "0.0.1"

@app.get('/', tags=['home'])
def home():
    return HTMLResponse('<h1>Hello Railway!!!!</h1>')

