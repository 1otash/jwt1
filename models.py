from pydantic import BaseModel

# Models for entry to account(login)
class LoginModel(BaseModel):
    username: str
    password: str


# Models for registration
class RegistrationModel(BaseModel):
    username: str
    password: str
    email: str


class Token(BaseModel):
    access_token: str
    token_type: str