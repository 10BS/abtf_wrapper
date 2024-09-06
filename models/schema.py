from typing import Literal, Optional

from pydantic import BaseModel, Field


class ItemsGameURL(BaseModel):
    success: bool
    file: str = Field(alias="value")


class ItemQualities(BaseModel):
    success: bool
    indexes: dict[str, int] = Field(alias="value")


class ItemQualityNames(BaseModel):
    success: bool
    qualities: dict[str, str] = Field(alias="value")


class Origin(BaseModel):
    index: int = Field(alias="origin")
    name: str


class ItemOrigins(BaseModel):
    success: bool
    origins: list[Origin] = Field(alias="value")


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


class ItemAttributes(BaseModel):
    success: bool
    attributes: list[ItemAttribute] = Field(alias="value")


class Attribute(BaseModel):
    name: str
    attr_class: str = Field(alias="class")
    value: int | float


class Set(BaseModel):
    item_set: str
    name: str
    items: list[str]
    attributes: Optional[list[Attribute]] = None


class ItemSets(BaseModel):
    success: bool
    sets: list[Set] = Field(alias="value")


class Particle(BaseModel):
    system: str
    id: int
    attach_to_rootbone: bool
    name: str


class AttachedParticles(BaseModel):
    success: bool
    particles: list[Particle] = Field(alias="value")


class Level(BaseModel):
    level: int
    required_score: int
    name: str


class LevelName(BaseModel):
    name: str
    levels: list[Level]


class ItemLevels(BaseModel):
    success: bool
    level_names: list[LevelName] = Field(alias="value")


class Counter(BaseModel):
    type: int
    type_name: str
    level_data: str


class Counters(BaseModel):
    success: bool
    counters: list[Counter] = Field(alias="value")


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


class Style(BaseModel):
    name: str


class Items(BaseModel):
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
    styles: list[Style]
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


class PaintKits(BaseModel):
    success: bool
    paints: dict[int, str]


class SchemaProperty(BaseModel):
    values: dict[str | int, str | int] | list[str]
