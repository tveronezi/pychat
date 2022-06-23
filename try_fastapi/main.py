import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/v1/system/ping")
async def root():
    return {"message": "pong"}

def start():
    uvicorn.run("try_fastapi.main:app", host="0.0.0.0", port=8000, reload=True)
    
