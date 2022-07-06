from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routers import user, career, auth
from utils import kmeans

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

app.include_router(user.router)
app.include_router(career.router)
app.include_router(auth.router)

@app.get('/test')
def test_kmeans():
    return {'data': kmeans.predict()}

@app.get('/dashboard')
async def dashboard(request: Request):
    return templates.TemplateResponse("admin/dashboard.html", {"request": request})

@app.exception_handler(404)
async def custom_404_handler(request, __):
    return templates.TemplateResponse("404.html", {"request": request})