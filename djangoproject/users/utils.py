import os
from http import HTTPStatus
import requests
from typing import Union


def get_user_data(user_nickname: str): # TODO change to response
    token = os.getenv("TOKEN")
    request = requests.get("https://open.faceit.com/data/v4/players", headers={"Authorization": f"Bearer {token}"},
                           params={"nickname": user_nickname})
    if request.status_code == HTTPStatus.OK:
        return request.json()
    return False

