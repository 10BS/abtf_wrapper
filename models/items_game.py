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


class LogicOptions(BaseModel):
    type: str
    value: Optional[str, None] = None
    player_key: Optional[str, None] = None
    get_player: Optional[str, None] = None
    is_owner: Optional[int, None] = None
    team_key: Optional[str, None] = None
    team_requirement: Optional[int, None] = None
    distance_check_type: Optional[int, None] = None
    distance_to_check: Optional[int, None] = None
    key_to_lookup: Optional[str, None] = None


class ConditionLogic(BaseModel):
    pass
