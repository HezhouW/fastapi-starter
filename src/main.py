import uvicorn
from fastapi import FastAPI, HTTPException,Request
from fastapi.exception_handlers import http_exception_handler
from loguru import logger

from appinit import init_app
app = FastAPI()
app =init_app(app)


@app.exception_handler(HTTPException)
async def validation_exception_handler(request: Request, exc):
    logger.error("OPS!!")
    return await http_exception_handler(request, exc)
@app.get("/")
async def root():
    return "welcome to fastapi skeleton"


# if __name__ == "__main__":
#     uvicorn.run(app="main:app", host='0.0.0.0', port=8000, reload=True)