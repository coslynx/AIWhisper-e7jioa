import uvicorn
from fastapi import FastAPI
from src.api.routes import api_router
from loguru import logger

app = FastAPI()
app.include_router(api_router)

@app.on_event("startup")
async def startup_event():
    logger.add("app.log", rotation="10 MB", level="DEBUG")
    logger.info("Application startup")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutdown")

if __name__ == "__main__":
    try:
        uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
    except Exception as e:
        logger.exception(f"Error during server startup: {e}")
```