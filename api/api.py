
from fastapi import FastAPI
from handlers import demo


def create_app():
    app = FastAPI(docs_url="/")

    # Routers
    app.include_router(demo.router)

    return app
