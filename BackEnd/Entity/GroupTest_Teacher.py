from fastapi import WebSocket


class GroupTest_Teacher:
    def __init__(self, websocket: WebSocket):
        self.websocket = websocket
        self.teacher = None
        self.room = None

    def set_room(self, room):  # room: Room_GroupTest
        self.room = room
        return self

    def get_room(self):  # -> Room_GroupTest
        return self.room

    def set_teacher(self, teacher):
        self.teacher = teacher
        return self

    def get_teacher(self):
        return self.teacher
