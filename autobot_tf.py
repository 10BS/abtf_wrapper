import json
from typing import Literal

from models.item_name_sku import ItemNames, ItemSkus
from models.item_object import ItemObjects
from models.schema import ItemOrigins, ItemAttributes, ItemSets, SchemaProperty
from utils import request
from utils.check_type import CheckType


class AutobotTF:
    @staticmethod
    def get_schema() -> None:
        headers = {
            "accept": "*/*"
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
    def schema_refresh() -> None:
        request.make_request(
            method="PATCH",
            base_url="https://schema.autobot.tf/",
            url="schema/refresh"
        )

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
    def get_name(
        items: str | dict | list[str | dict],
        get_from: Literal["item_object", "sku"]
    ) -> ItemNames:
        bulk: bool = True if isinstance(items, list) else False
        headers = {
            "accept": "*/*",
        }
        if bulk:
            headers["Content-Type"] = "application/json"
        method_mapping = {
            "item_object": "fromItemObjectBulk" if bulk else f"fromItemObject",
            "sku": "fromSkuBulk" if bulk & CheckType.is_list_of(items, str) else f"fromSku/{items.replace(";", "%3B")}",
        }
        method = method_mapping.get(get_from)
        response = request.make_request(
            method="GET" if get_from == "name" and not bulk else "POST",
            base_url="https://schema.autobot.tf/",
            url=f"getSku/{method}",
            headers=headers,
            json=items,
            output="json",
        )
        return ItemNames(**response)

    @staticmethod
    def get_sku(
        items: str | dict | list[str | dict],
        get_from: Literal["item_object", "name", "econ_item"]
    ) -> ItemSkus:
        bulk: bool = True if isinstance(items, list) else False
        headers = {
            "accept": "*/*",
        }
        if bulk:
            headers["Content-Type"] = "application/json"
        method_mapping = {
            "item_object": "fromItemObjectBulk" if bulk else f"fromItemObject",
            "name": "fromNameBulk" if bulk & CheckType.is_list_of(items, str) else f"fromName/{items}",
            "econ_item": "fromEconItemBulk" if bulk & CheckType.is_list_of(items, dict) else "fromEconItem"
        }
        method = method_mapping.get(get_from)
        response = request.make_request(
            method="GET" if get_from == "sku" and not bulk else "POST",
            base_url="https://schema.autobot.tf/",
            url=f"getSku/{method}",
            headers=headers,
            json=items,
            output="json",
        )
        return ItemSkus(**response)

    @staticmethod
    def get_item_object(
        items: str | dict | list[str | dict],
        get_from: Literal["name", "sku", "econ_item"],
    ) -> ItemObjects:
        bulk: bool = True if isinstance(items, list) else False
        if isinstance(items, dict) | CheckType.is_list_of(items, dict):
            return AutobotTF.__from_econ_items(items, bulk)
        headers = {
            "accept": "*/*",
        }
        if bulk:
            headers["Content-Type"] = "application/json"
        method_mapping = {
            "name": "fromNameBulk" if bulk else f"fromName/{items}",
            "sku": "fromSkuBulk" if bulk else f"fromSku/{items.replace(";", "%3B")}",
        }
        method = method_mapping.get(get_from)
        response = request.make_request(
            method="POST" if bulk else "GET",
            base_url="https://schema.autobot.tf/",
            url=f"getItemObject/{method}",
            headers=headers,
            json=items if bulk else None,
            output="json",
        )
        return ItemObjects(**response)

    @staticmethod
    def __from_econ_items(
        items: dict | list[dict],
        bulk: bool
    ) -> ItemObjects:
        headers = {
            "accept": "*/*",
            "Content-Type": "application/json",
        }
        response = request.make_request(
            method="POST",
            base_url="https://schema.autobot.tf/getItemObject/",
            url="fromEconItem" if not bulk else "fromEconItemBulk",
            headers=headers,
            json=items,
            output="json",
        )
        return ItemObjects(**response)
