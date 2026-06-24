from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):

    projects = [
        {
            "name": "Personal Portfolio",
            "description": "Portfolio website built with FastAPI and Jinja2",
            "status": "Production"
        },
        {
            "name": "Network Scanner",
            "description": "Network discovery and port scanning tool",
            "status": "Active Development"
        },

    ]
    certifications = [
        {
            "name": "OSHA 10",
            "issuer": "OSHA",
            "description": "Workplace safety and health training."
        },
        {
            "name": "OSHA 30",
            "issuer": "OSHA",
            "description": "Advanced workplace safety and hazard prevention training."
        }
    ]
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "projects": projects,
            "certifications": certifications
        }
    )