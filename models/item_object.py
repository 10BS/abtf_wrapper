from typing import Optional

from pydantic import BaseModel, Field, AliasChoices


class Item(BaseModel):
    def_index: int = Field(alias="defindex")
    quality: int
    craftable: bool
    tradable: bool
    killstreak: int
    australium: bool
    effect: Optional[int] = None
    festive: bool
    paint_kit: Optional[int] = Field(default=None, alias="paintkit")
    wear: Optional[int] = None
    quality2: Optional[int] = None
    craft_number: Optional[int] = Field(default=None, alias="craftnumber")
    crate_series: Optional[int] = Field(default=None, alias="crateseries")
    target: Optional[int] = None
    output: Optional[int] = None
    output_quality: Optional[int] = Field(default=None, alias="outputQuality")
    paint: Optional[int] = None


class ItemObjects(BaseModel):
    success: bool
    item_objects: Item | list[Item] = Field(
        validation_alias=AliasChoices("item", "itemObject", "itemObjects")
    )
