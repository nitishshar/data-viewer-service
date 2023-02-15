import uvicorn

from api.api import create_app


def main():
    app = create_app()
    uvicorn.run(app, port=8080, host="127.0.0.1")


if __name__ == "__main__":
    main()
