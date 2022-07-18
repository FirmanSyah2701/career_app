from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import admin, career, auth, web
from core.config import templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(admin.router)
app.include_router(career.router)
app.include_router(auth.router)
app.include_router(web.router)

@app.exception_handler(404)
async def custom_404_handler(request, __):
    return templates.TemplateResponse("404.html", {"request": request})