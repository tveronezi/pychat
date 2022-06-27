from pydantic import BaseModel as PydanticBaseModel


class BaseModel(PydanticBaseModel):
    class Config:
        # This parameter is in beta
        # https://pydantic-docs.helpmanual.io/usage/model_config/#options
        frozen = True
