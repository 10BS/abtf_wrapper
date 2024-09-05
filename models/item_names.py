from pydantic import BaseModel, Field


class FromItemObject(BaseModel):
    success: bool
    name: str


class FromItemObjectBulk(BaseModel):
    success: bool
    names: list[str] = Field(alias="itemNames")


class FromSku(BaseModel):
    success: bool
    name: str


class FromSkuBulk(BaseModel):
    success: bool
    names: list[str] = Field(alias="itemNames")
