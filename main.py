from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/profile")
async def profile():
    return {
        "name": "Jhonny",
        "job": "Data Center Technician",
        "location": "Columbus"
    }

@app.get("/skills")
async def skills():
    return {
        "skills": [
            "Fiber Optics",
            "Linux",
            "Networking",
            "Python"
        ]
    }