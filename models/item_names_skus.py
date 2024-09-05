from pydantic import BaseModel, Field


class ItemName(BaseModel):
    success: bool
    name: str


class ItemNames(BaseModel):
    success: bool
    names: list[str] = Field(alias="itemNames")


class ItemSku(BaseModel):
    success: bool
    sku: str


class ItemSkus(BaseModel):
    success: bool
    skus: list[str]
