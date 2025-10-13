from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="SmartClimateForecast")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/predict", response_class=HTMLResponse)
async def predict_page(request: Request):
    return templates.TemplateResponse("prediction.html", {"request": request})

@app.get("/faq", response_class=HTMLResponse)
async def faq(request: Request):
    return templates.TemplateResponse("faq.html", {"request": request})
