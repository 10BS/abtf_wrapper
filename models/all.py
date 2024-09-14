from typing import ClassVar

from pydantic import BaseModel, Field, AliasChoices

from models.item_object import ItemObject
from models.items_game import ItemsGameItems
from models.schema import SchemaItem, ItemAttribute, Origin, Attribute, Set, Particle, LevelName, Counter, StringLookups


class ItemNames(BaseModel):
    success: bool
    names: str | list[str] = Field(validation_alias=AliasChoices("name", "itemNames"))


class ItemSkus(BaseModel):
    success: bool
    skus: str | list[str] = Field(validation_alias=AliasChoices("sku", "skus"))


class ItemObjects(BaseModel):
    success: bool
    item_objects: ItemObject | list[ItemObject] = Field(
        validation_alias=AliasChoices("item", "itemObject", "itemObjects")
    )


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
    success: bool
    schema_items: SchemaItem = Field(alias="schemaItems")
    items_game_items: ItemsGameItems = Field(alias="items_gameItems")


class TryItems(BaseModel):
    items: dict[int | str, ItemsGameItems]
