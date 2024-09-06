import json
from typing import Literal

from pydantic import Field

import request
from models.item_name_sku import ItemName
from models.item_object import ItemObjects
from models.schema import ItemOrigins, ItemAttributes, ItemSets, SchemaProperty


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
            output="json",
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
            output="json",
        )
        return ItemOrigins(**response)

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
            output="json",
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
            output="json",
        )
        return ItemSets(**response)

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
            output="json",
        )
        return SchemaProperty(values=response)

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
            output="json",
        )
        return ItemName(**response).name

    @staticmethod
    def get_item_object(
        items: str | list[str],
        bulk: bool,
        get_from: Literal["name", "sku", "econ_item"],
    ) -> ItemObjects:
        headers = {
            "accept": "*/*",
        }
        if bulk:
            headers["Content-Type"] = "application/json"
        method_mapping = {
            "name": "fromNameBulk" if bulk else f"fromName/{items}",
            "sku": "fromSkuBulk" if bulk else f"fromSku/{items}",
            "econ_item": "fromEconItem" if bulk else f"fromEconItem/{items}"
        }
        method = method_mapping.get(get_from)
        response = request.make_request(
            method="POST",
            base_url="https://schema.autobot.tf/",
            url=f"getItemObject/{method}",
            headers=headers,
            json=items if bulk else None,
            output="json",
        )
        return ItemObjects(**response)
