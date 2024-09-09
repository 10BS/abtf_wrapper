from pydantic import BaseModel, Field, AliasChoices
from typing import Optional


class Rarity(BaseModel):
    value: int
    loc_key: str
    loc_key_weapon: str
    color: str
    loot_list: Optional[str, None]
    drop_sound: Optional[str, None]
    next_rarity: Optional[str, None]


class Value(BaseModel):
    success: bool
    value: dict[str | int, dict[str | int, str | int | Rarity]]


class GameInfo(BaseModel):
    success: bool
    values: dict[str, int] = Field(alias="value")


class Qualities(BaseModel):
    success: bool
    values: dict[str, dict[str, int | str]] = Field(alias="value")


class Rarities(BaseModel):
    success: bool
    values: dict[str, Rarity] = Field(alias="value")


class EquipRegionsList(BaseModel):
    success: bool
    values: dict[str, int | dict[str, int]] = Field(alias="value")


class EquipConflicts(BaseModel):
    success: bool
    values: dict[str, dict[str, int]] = Field(alias="value")
