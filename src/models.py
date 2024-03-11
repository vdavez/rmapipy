from pydantic import BaseModel, Field
from uuid import uuid4


class DeviceToken(BaseModel):
    token: str


class DeviceTokenRequest(BaseModel):
    code: str
    deviceDesc: str = Field(default="desktop-linux")
    deviceID: str = Field(default_factory=lambda: str(uuid4()))


class UserToken(BaseModel):
    token: str
