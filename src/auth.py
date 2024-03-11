import httpx
from .models import *


def register_device(code: str) -> DeviceToken:
    url = "https://webapp-prod.cloud.remarkable.engineering/token/json/2/device/new"
    req = models.DeviceTokenRequest(code=code)
    headers = {"user-agent": "rmapipy"}
    res = httpx.post(url, headers=headers, json=req)
    return DeviceToken(token=res.text)


def register_user(DeviceToken) -> UserToken:
    url = "https://webapp-prod.cloud.remarkable.engineering/token/json/2/user/new"
    headers = {"Authorization": f"Bearer {DeviceToken.token}"}
    res = httpx.post(url, headers=headers)
    return UserToken(token=res.text)
