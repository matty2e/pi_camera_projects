import asyncio
from typing import Optional

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse


class CameraApi:
    def __init__(self):
        self.version = "0.0.1"

        url = "https://stackoverflow.com/q/65446591/5538913"
        self.app = FastAPI(
            title="FastAPI from class",
            description=f"Source: <a href='{url}'>Stack Overflow</a>",
        )
        self.serving_task: Optional[asyncio.Task] = None

    async def serve(self):
        app: FastAPI = self.app

        @app.get("/", include_in_schema=False)
        async def _get_root():
            """
            Redirect to /docs
            """
            return HTMLResponse('<meta http-equiv="Refresh" content="0; url=\'/docs\'" />')

        @app.get("/version")
        async def _get_version() -> JSONResponse:
            return JSONResponse({"MyClass version": self.version, "FastAPI version": app.version})

        # serve
        config = uvicorn.Config(app, host="127.0.0.1", port=8000)
        server = uvicorn.Server(config)
        await server.serve()


if __name__ == "__main__":
    instance = CameraApi()
    asyncio.run(instance.serve())


