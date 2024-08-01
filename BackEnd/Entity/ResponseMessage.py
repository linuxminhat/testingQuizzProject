class ResponseMessage:
    def __init__(self, status=None, message=None):
        self._status = status
        self._message = message

    def set_status(self, status):
        self._status = status
        return self

    def set_message(self, message):
        self._message = message
        return self

    def serialize(self):
        return {
            'status': self._status,
            'message': self._message
        }
