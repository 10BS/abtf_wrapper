from pydantic import BaseModel, Field, AliasChoices


class ItemNames(BaseModel):
    success: bool
    names: str | list[str] = Field(validation_alias=AliasChoices("name", "itemNames"))


class ItemSkus(BaseModel):
    success: bool
    skus: str | list[str] = Field(validation_alias=AliasChoices("sku", "skus"))
