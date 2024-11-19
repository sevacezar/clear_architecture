import re

from pydantic import BaseModel, Field, EmailStr, field_validator


class UserDTO(BaseModel):
    name: str
    email: EmailStr
    phone: str
    password: str
    is_admin: bool = Field(default=False)


class CreateUserDTO(UserDTO):

    @field_validator('phone')
    @classmethod
    def validate_phone(cls, phone):
        if not isinstance(phone, [str, int]):
            raise TypeError('Invalid phone type value')
        phone_regex = re.compile(r'\+?\d{11}')
        if not phone_regex.match(str(phone)):
            raise ValueError('Invalid phone number')
        return phone

class GetUserDTO(UserDTO):
    id: int

    class Config:
        orm_mode = True

class GetMultipleUsersDTO(BaseModel):
    users: list[GetUserDTO]
