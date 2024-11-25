from fastapi import FastAPI

from api.fastapi.users.routers import router as user_router

def get_fastapi_app() -> FastAPI:
    app: FastAPI = FastAPI()
    app.include_router(user_router)

    return app

