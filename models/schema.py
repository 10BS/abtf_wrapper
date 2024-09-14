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


class Capability(BaseModel):
    nameable: bool
    can_gift_wrap: bool
    can_craft_mark: bool
    can_be_restored: bool
    strange_parts: bool
    can_card_upgrade: bool
    can_strangify: bool
    can_killstreakify: bool
    can_consume: bool


class SchemaItem(BaseModel, extra="allow"):
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
    capabilities: Capability
    styles: list[dict[str, str]]
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
    attributes: ClassVar[list[Attribute]]


class GenericResponseModel(BaseModel, extra="allow"):
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
