from flask import Response


class ResponseEntity(Response):
    def __init__(self, response, status=None):
        super().__init__(content_type='application/json', status=200 if status is None else status, response=response)
