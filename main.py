import logging

from fastapi import FastAPI, Response

logger = logging.getLogger("uvicorn.error")
logger.info("API is starting up")

app = FastAPI()


@app.get("/")
def main():
    logger.debug("this is a debug message")
    return Response(content="Hello from Fastapi!", media_type="text/plain")


if __name__ == "__main__":
    main()
