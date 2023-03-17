import asyncio

from fastapi import FastAPI, APIRouter, WebSocket
from starlette.websockets import WebSocketDisconnect
from uvicorn import Server, Config

from domain.models.calculator import Calculator
from infrastructure.dto.factorial import FactorialData
from infrastructure.providers.base import BaseProvider
from infrastructure.utils import HighLoadTask


class HttpProvider(BaseProvider):

    def __init__(self):
        self.web_app = FastAPI(title="Universal BPM", debug=True)
        self.web_server = Server(config=Config(app=self.web_app, host="localhost", port=8888))
        self.add_routes()

    @classmethod
    async def factorial_websocket(cls, websocket: WebSocket):
        await websocket.accept()
        try:
            while True:
                msg = await websocket.receive_text()
                try:
                    factorial_data = FactorialData.from_raw_msg(msg=msg)
                    result = await HighLoadTask.execute(Calculator.factorial, factorial_data.number)
                    await websocket.send_text(result)
                except TypeError as err:
                    await websocket.send_text(str(err))

        except WebSocketDisconnect:
            await websocket.send_text("Connection closed")
            await websocket.close()

    def add_routes(self):
        router = APIRouter()
        router.add_api_websocket_route("/ws/factorial", self.factorial_websocket)
        self.web_app.include_router(router, prefix="/api")

    async def run(self):
        try:
            await self.web_server.serve()
        except asyncio.CancelledError:
            await self.web_server.shutdown()
