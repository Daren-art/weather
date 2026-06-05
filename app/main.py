from fastapi import FastAPI
from fastapi import Request
from fastapi import Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.weather_service import get_weather

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request,name="index.html")

@app.post("/", response_class=HTMLResponse)
async def weather(request: Request,city: str = Form(...)):
    data = await get_weather(city)
    return templates.TemplateResponse(request=request,name="weather.html",context={"weather": data})