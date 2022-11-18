from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    name: str = Field(default=None)
    phone: str = Field(default=None)
    email: EmailStr


class UserInDBSchema(UserSchema):
    id: int = Field(ge=1)
