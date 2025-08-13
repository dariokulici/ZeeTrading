from fastapi import FastAPI, APIRouter
from routers.auth import router as auth_router

app = FastAPI()

# auth Route
app.include_router(auth_router)
