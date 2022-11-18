from pydantic import BaseModel


class ConfigSchema(BaseModel):
    DATABASE: str
