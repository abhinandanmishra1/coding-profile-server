from pydantic import BaseModel

class LeetcodeRequestBody(BaseModel):
    username: str