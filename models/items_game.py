from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Rarity(BaseModel):
    value: int
    loc_key: str
    loc_key_weapon: str
    color: str
    loot_list: Optional[str]
    drop_sound: Optional[str]
    next_rarity: Optional[str]


class ConditionLogic(BaseModel):
    type: str
    value: Optional[str] = None
    player_key: Optional[str] = None
    get_player: Optional[str] = None
    is_owner: Optional[int] = None
    team_key: Optional[str] = None
    team_requirement: Optional[int] = None
    distance_check_type: Optional[int] = None
    distance_to_check: Optional[int] = None
    key_to_lookup: Optional[str] = None


class Quest(BaseModel):
    name: str
    condition_logic: dict[str, dict[str, ConditionLogic]]
    type: str
    event_name: Optional[str] = None
    score_key_name: Optional[str] = None


class QuestObjectiveConditions(BaseModel):
    success: bool
    value: dict[str, Quest]


class CardType(BaseModel):
    value: int
    loc_key: str
    ui: str


class ItemCollection(BaseModel):
    name: str
    description: str
    is_reference_collection: int
    items: dict[str, int | dict[str, int]]


class Operation(BaseModel):
    name: str
    operation_start_date: datetime
    stop_adding_to_queue_date: datetime
    stop_giving_to_player_date: datetime
    contracts_end_date: datetime
    operation_loot_list: str = Field(alias="operation_lootlist")
    is_campaign: Optional[int] = None
    max_drop_count: Optional[int] = None
    uses_credits: Optional[int] = None


class RespondModel(BaseModel):
    success: bool
    value: dict[str | int, dict[str | int, str | int] | Rarity | CardType | ItemCollection | Operation]
