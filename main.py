import uvicorn
from app.api.endpoints import router  # Import your FastAPI router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)  # Include your router in the FastAPI app

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
