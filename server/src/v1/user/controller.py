from flask import request, make_response, jsonify
from v1.user.model import UserModel
from v1.basecontroller import BaseController


class UserController(BaseController):
    _instance = None

    def __init__(self) -> None:
        self._instance = UserModel()

    def check(self, username, password):
        # check if username or password is a string
        if not isinstance(username, str) or not isinstance(password, str):
            return False

        # check if username is empty
        if(len(username) == 0):
            return False

        resp = self._instance.query(username, password)
        if resp:
            return True
        else:
            return False
