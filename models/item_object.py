from pydantic import BaseModel, Field
from typing import Optional


class Item(BaseModel):
    defindex: int
    quality: int
    craftable: bool
    tradable: bool
    killstreak: int
    australium: bool
    effect: Optional[int] = None
    festive: bool
    paintkit: Optional[int] = None
    wear: Optional[int] = None
    quality2: Optional[int] = None
    craftnumber: Optional[int] = None
    crateseries: Optional[int] = None
    target: Optional[int] = None
    output: Optional[int] = None
    outputQuality: Optional[int] = None
    paint: Optional[int] = None


class ItemObject(BaseModel):
    success: bool
    item: dict[Item]


class ItemObjects(BaseModel):
    success: bool
    items: list[Item]
