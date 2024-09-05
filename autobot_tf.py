import json

from pydantic import Field

import request
from models.item_name_sku import ItemName
from models.item_object import ItemObjects
from models.schema import (
    ItemOrigins,
    ItemAttributes,
    ItemSets,
    SchemaProperty
)


class AutobotTF:
    @staticmethod
    def get_schema() -> None:
        headers = {
            "accept": "*/*",
        }
        response = request.make_request(
            method="GET",
            base_url="https://schema.autobot.tf/",
            url="schema/download",
            headers=headers,
            mode="json"
        )
        with open("schema.json", "w", encoding="utf-8") as schema:
            json.dump(response, schema, indent=4)

    @staticmethod
    def get_origins() -> ItemOrigins:
        headers = {
            "accept": "*/*",
        }
        response = request.make_request(
            method="GET",
            base_url="https://schema.autobot.tf/",
            url="raw/schema/originNames",
            headers=headers,
            mode="json"
        )
        data = ItemOrigins(**response)
        return data

    @staticmethod
    def get_attributes() -> ItemAttributes:
        headers = {
            "accept": "*/*",
        }
        response = request.make_request(
            method="GET",
            base_url="https://schema.autobot.tf/",
            url="raw/schema/attributes",
            headers=headers,
            mode="json"
        )
        data = ItemAttributes(**response)
        return data

    @staticmethod
    def get_sets() -> ItemSets:
        headers = {
            "accept": "*/*",
        }
        response = request.make_request(
            method="GET",
            base_url="https://schema.autobot.tf/",
            url="raw/schema/item_sets",
            headers=headers,
            mode="json"
        )
        data = ItemSets(**response)
        return data

    @staticmethod
    def get_schema_property() -> SchemaProperty:
        headers = {
            "accept": "*/*",
        }
        response = request.make_request(
            method="GET",
            base_url="https://schema.autobot.tf/",
            url="properties/wears",
            headers=headers,
            mode="json"
        )
        data = SchemaProperty(values=response)
        return data

    @staticmethod
    def name_from_sku(sku: str = Field(min_length=1)) -> str:
        headers = {
            "accept": "*/*",
        }
        response = request.make_request(
            method="GET",
            base_url="https://schema.autobot.tf/",
            url=f"getName/fromSku/{sku.replace(";", "%3B")}",
            headers=headers,
            mode="json"
        )
        item_name = ItemName(**response)
        return item_name.name

    @staticmethod
    def get_item_object(items: list[str]) -> ItemObjects:
        headers = {
            "accept": "*/*",
            "Content-Type": "application/json",
        }
        response = request.make_request(
            method="POST",
            base_url="https://schema.autobot.tf/",
            url="getItemObject/fromNameBulk",
            headers=headers,
            data=items,
            mode="json"
        )
        data = ItemObjects(**response)
        return data
