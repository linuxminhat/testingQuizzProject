from fastapi import WebSocket
from Backend.Model.DB_model import Teacher


class TeacherWS:
    def __init__(self, websocket: WebSocket, teacher: Teacher):
        self.websocket = websocket
        self.teacher = teacher

    async def send_text(self, text: str):
        await self.websocket.send_text(text)

    async def send_json(self, data: dict):
        await self.websocket.send_json(data)
