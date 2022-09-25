class Response:
    def __init__(self, success:int, message="", errors:list=[], data={}):
        self.success = success
        self.message = message
        self.errors = errors
        self.data = data