from datetime import datetime
from typing import Literal, Optional, ClassVar

from pydantic import BaseModel, Field, AliasChoices


class ItemAttribute(BaseModel):
    name: str
    def_index: int = Field(alias="defindex")
    attribute_class: Optional[str] = None
    description_string: Optional[str] = None
    description_format: Optional[str] = None
    effect_type: Literal[
        "positive",
        "negative",
        "neutral",
        "unusual",
        "strange",
        "value_is_from_lookup_table",
    ]
    hidden: bool
    stored_as_integer: bool


class Origin(BaseModel):
    index: int = Field(alias="origin")
    name: str


class Attribute(BaseModel):
    name: str
    attr_class: str = Field(alias="class")
    value: int | float


class Set(BaseModel):
    item_set: str
    name: str
    items: list[str]
    attributes: Optional[list[Attribute]] = None


class Particle(BaseModel):
    system: str
    id: int
    attach_to_rootbone: bool
    name: str


class Level(BaseModel):
    level: int
    required_score: int
    name: str


class LevelName(BaseModel):
    name: str
    levels: list[Level]


class Counter(BaseModel):
    type: int
    type_name: str
    level_data: str


class String(BaseModel):
    index: int
    string: str


class TableName(BaseModel):
    table_name: str
    strings: list[String]


class StringLookups(BaseModel):
    success: bool
    table_names: list[TableName] = Field(alias="value")


class Capabilities(BaseModel):
    nameable: bool
    can_gift_wrap: bool
    can_craft_mark: bool
    can_be_restored: bool
    strange_parts: bool
    can_card_upgrade: bool
    can_strangify: bool
    can_killstreakify: bool
    can_consume: bool


class SchemaItem(BaseModel):
    name: str
    def_index: int = Field(alias="defindex")
    item_class: str
    item_type_name: str
    item_name: str
    proper_name: bool
    item_slot: str
    player_model: Optional[str] = Field(default=None, alias="model_player")
    item_quality: int
    image_inventory: str
    min_item_level: int = Field(ge=1, le=100, alias="min_ilevel")
    max_item_level: int = Field(ge=1, le=100, alias="max_ilevel")
    image_url: str
    image_url_large: str
    drop_type: Optional[Literal["none", "drop"]] = None
    craft_class: str
    craft_material_type: str
    capabilities: Capabilities
    styles: list[dict["name", str]]
    used_by_classes: list[
        Literal[
            "Scout",
            "Soldier",
            "Pyro",
            "Demoman",
            "Heavy",
            "Engineer",
            "Medic",
            "Sniper",
            "Spy",
        ]
    ]
    attributes: list[Attribute]


class ItemsGameItems(BaseModel):
    name: str
    first_sale_date: datetime
    prefab: str
    capabilities: dict[str, int]
    equip_regions: dict[str, int]
    item_name: str
    item_type_name: str
    image_inventory: str
    player_model: str = Field(alias="model_player")
    drop_type: str
    used_by_classes: dict[str, int]
    mouse_pressed_sound: str
    drop_sound: str


class GenericResponseModel(BaseModel):
    success: ClassVar[bool]
    values: (
        str
        | int
        | list[
            str
            | ItemAttribute
            | Origin
            | Attribute
            | Set
            | Particle
            | LevelName
            | Counter
            | StringLookups
        ]
        | dict[str | int, str | int]
    ) = Field(validation_alias=(AliasChoices("value", "grade", "items")))


class Item(BaseModel):
    success: ClassVar[bool]
    schema_items: SchemaItem = Field(alias="schemaItems")
    items_game_items: ItemsGameItems = Field(alias="items_gameItems")
