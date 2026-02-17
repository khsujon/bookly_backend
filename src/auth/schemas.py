from pydantic import BaseModel, Field



class UserCreateModel(BaseModel):
    username : str = Field(max_length=50)
    email : str = Field(max_length=255)
    password : str = Field(min_length=8, max_length=128)
    