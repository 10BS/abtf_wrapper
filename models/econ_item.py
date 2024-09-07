from typing import Optional

from pydantic import BaseModel, Field


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
    quantity: Optional[int] = None
    def_index: int
    quality: int
    limited: Optional[str] = None
    slot: Optional[int] = None
    filter_data: Optional[FilterData] = None


class EconItem(BaseModel):
    app_id: int = Field(default=None, alias="appid")
    context_id: Optional[int] = Field(default=None, alias="contextid")
    asset_id: Optional[int] = Field(default=None, alias="assetid")
    id: Optional[int] = None
    class_id: Optional[int] = Field(default=None, alias="classid")
    instance_id: int = Field(alias="instanceid")
    amount: Optional[str] = None
    pos: Optional[int] = None
    missing: Optional[bool] = None
    currency: Optional[int] = None
    background_color: str
    icon_url: str
    icon_url_large: str
    icon_drag_url: Optional[str] = None
    descriptions: list[Description]
    tradable: int
    actions: Optional[list[Action]] = None
    fraud_warnings: Optional[list[str]] = Field(default=None, alias="fraudwarnings")
    name: str
    name_color: str
    type: str
    market_name: str
    market_hash_name: str
    market_actions: Optional[list[Action]] = None
    commodity: int
    market_tradable_restriction: int
    market_marketable_restriction: int
    marketable: int
    tags: list[Tag]
    app_data: AppData
    owner_descriptions: Optional[list[str]] = None
    owner_actions: Optional[list[str]] = None


class EconItems(BaseModel):
    values: list[EconItem]
