from fastapi import WebSocket

from Backend.WebSocket.Business.Room_Manager import Room_Manager
from Backend.WebSocket.Business.BO_Student_Message import BO_Student_Message
from Backend.WebSocket.Business.BO_Teacher_Message import BO_Teacher_Message
from Backend.Router import app
from Backend.WebSocket.Entity.GroupTest_Student import GroupTest_Student
from Backend.WebSocket.Entity.TeacherWS import TeacherWS


@app.websocket("/student")
async def student_endpoint(websocket: WebSocket):
    await BO_Student_Message(websocket).handle()


@app.websocket("/teacher")
async def teacher_endpoint(websocket: WebSocket):
    await BO_Teacher_Message(websocket).handle()