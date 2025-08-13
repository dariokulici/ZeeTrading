from pydantic import BaesModel

class UserBase(BaseModel):
    user_uuid: str
    user_name: str
    user_password: str
    