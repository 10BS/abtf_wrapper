from typing import Optional

from pydantic import BaseModel, Field, AliasChoices


class Description(BaseModel):
    value: str
    color: Optional[str] = None
    app_data: Optional[dict[str, int]] = None


class Action(BaseModel):
    link: Optional[str] = None
    name: str


class Tag(BaseModel):
    internal_name: str
    name: str
    category: str
    color: Optional[str] = None
    category_name: str
    localized_tag_name: Optional[str] = None
    localized_category_name: Optional[str] = None


class FilterData(BaseModel):
    player_class_ids: list[str]
    highlight_color: str


class AppData(BaseModel):
    quantity: int
    def_index: int
    quality: int
    limited: Optional[str] = None
    slot: Optional[int] = None
    filter_data: FilterData


class EconItems(BaseModel):
    app_id: int = Field(alias="appid")
    context_id: str = Field(alias="contextid")
    asset_id: str = Field(alias="assetid")
    id: str
    class_id: str = Field(alias="classid")
    instance_id: str = Field(alias="instanceid")
    amount: str
    pos: int
    missing: bool
    currency: int
    background_color: str
    icon_url: str
    icon_url_large: str
    icon_drag_url: Optional[str] = None
    descriptions: list[Description]
    tradable: int
    actions: list[Action]
    fraud_warnings: list[str] = Field(alias="fraudwarnings")
    name: str
    name_color: str
    type: str
    market_name: str
    market_hash_name: str
    market_actions: list[Action]
    commodity: int
    market_tradable_restriction: int
    market_marketable_restriction: int
    marketable: int
    tags: list[Tag]
    app_data: AppData
    owner_descriptions: list[str]
    owner_actions: list[str]
