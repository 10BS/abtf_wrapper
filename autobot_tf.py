import json
from typing import Any, Literal

import request
from models.all import (
    ItemNames,
    ItemSkus,
    ItemObjects,
    GenericResponseModel,
    Item,
)


class AutobotTF:
    @staticmethod
    def get_schema() -> None:
        headers = {"accept": "*/*"}
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
            method="PATCH", base_url="https://schema.autobot.tf/", url="schema/refresh"
        )

    @staticmethod
    def get_schema_key(
        key: Literal[
            "items_game_url",
            "qualities",
            "qualityNames",
            "originNames",
            "attributes",
            "item_sets",
            "attribute_controlled_attached_particles",
            "item_levels",
            "kill_eater_score_types",
            "string_lookups",
            "items",
            "paintkits",
        ]
    ) -> GenericResponseModel:
        headers = {"accept": "*/*"}
        response = request.make_request(
            method="GET",
            base_url="https://schema.autobot.tf/",
            url=f"raw/schema/{key}",
            headers=headers,
            output="json",
        )
        return GenericResponseModel(**response)

    @staticmethod
    def get_schema_property(
        property: Literal[
            "defindexes",
            "qualities",
            "killstreaks",
            "effects",
            "paintkits",
            "wears",
            "crateseries",
            "paints",
            "strangeParts",
            "craftWeapons",
            "uncraftWeapons",
            "craftWeaponsByClass/",
        ],
        class_char: (
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
            | None
        ) = None,
    ) -> GenericResponseModel:
        headers = {"accept": "*/*"}
        response = request.make_request(
            method="GET",
            base_url="https://schema.autobot.tf/properties/",
            url=(
                property + class_char
                if property == "craftWeaponsByClass/"
                else property
            ),
            headers=headers,
            output="json",
        )
        return GenericResponseModel(value=response)

    @staticmethod
    def get_name(
        items: str | dict | list[str | dict], get_from: Literal["item_object", "sku"]
    ) -> ItemNames:
        bulk: bool = True if isinstance(items, list) else False
        headers = {"accept": "*/*"}
        if bulk:
            headers["Content-Type"] = "application/json"
        method_mapping = {
            "item_object": "fromItemObjectBulk" if bulk else f"fromItemObject",
            "sku": (
                "fromSkuBulk"
                if bulk & AutobotTF.__is_list_of(items, str)
                else f"fromSku/{items.replace(";", "%3B")}"
            ),
        }
        from_ = method_mapping.get(get_from)
        response = request.make_request(
            method="GET" if get_from == "name" and not bulk else "POST",
            base_url="https://schema.autobot.tf/",
            url=f"getSku/{from_}",
            headers=headers,
            json=items,
            output="json",
        )
        return ItemNames(**response)

    @staticmethod
    def get_sku(
        items: str | dict | list[str | dict],
        get_from: Literal["item_object", "name", "econ_item"],
    ) -> ItemSkus:
        bulk: bool = True if isinstance(items, list) else False
        headers = {"accept": "*/*"}
        if bulk:
            headers["Content-Type"] = "application/json"
        method_mapping = {
            "item_object": "fromItemObjectBulk" if bulk else f"fromItemObject",
            "name": (
                "fromNameBulk"
                if bulk & AutobotTF.__is_list_of(items, str)
                else f"fromName/{items}"
            ),
            "econ_item": (
                "fromEconItemBulk"
                if bulk & AutobotTF.__is_list_of(items, dict)
                else "fromEconItem"
            ),
        }
        from_ = method_mapping.get(get_from)
        response = request.make_request(
            method="GET" if get_from == "sku" and not bulk else "POST",
            base_url="https://schema.autobot.tf/",
            url=f"getSku/{from_}",
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
        if isinstance(items, dict) | AutobotTF.__is_list_of(items, dict):
            return AutobotTF.__from_econ_items(items, bulk)
        headers = {"accept": "*/*"}
        if bulk:
            headers["Content-Type"] = "application/json"
        method_mapping = {
            "name": "fromNameBulk" if bulk else f"fromName/{items}",
            "sku": "fromSkuBulk" if bulk else f"fromSku/{items.replace(";", "%3B")}",
        }
        from_ = method_mapping.get(get_from)
        response = request.make_request(
            method="POST" if bulk else "GET",
            base_url="https://schema.autobot.tf/",
            url=f"getItemObject/{from_}",
            headers=headers,
            json=items if bulk else None,
            output="json",
        )
        return ItemObjects(**response)

    @staticmethod
    def __from_econ_items(items: dict | list[dict], bulk: bool) -> ItemObjects:
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

    @staticmethod
    def get_item_grade(
        items: int | str | None = None,
        get_from: Literal["def_index", "name", "sku"] | None = None,
    ) -> GenericResponseModel:
        headers = {"accept": "*/*"}
        method_mapping = {
            "def_index": f"fromDefindex/{items}",
            "name": f"fromName/{items}",
            "sku": f"fromSku/{items}",
        }
        from_ = method_mapping.get(get_from)
        response = request.make_request(
            method="GET",
            base_url="https://schema.autobot.tf/",
            url=f"getItemGrade/{from_}",
            headers=headers,
            output="json",
        )
        return GenericResponseModel(**response)

    @staticmethod
    def get_item_grades(v: Literal["v1", "v2"]) -> GenericResponseModel:
        headers = {"accept": "*/*"}
        response = request.make_request(
            method="GET",
            base_url="https://schema.autobot.tf/",
            url=f"getItemGrade/{v}",
            headers=headers,
            output="json",
        )
        return GenericResponseModel(**response)

    @staticmethod
    def get_item(
        items: str | int, get_from: Literal["def_index", "name", "sku"]
    ) -> Item:
        headers = {"accept": "*/*"}
        method_mapping = {
            "def_index": f"getItem/fromDefindex/{items}",
            "name": f"getItem/fromName/{items}",
            "sku": f"getItem/fromSku/{items}",
        }
        response = request.make_request(
            method="GET",
            base_url="https://schema.autobot.tf/",
            url=method_mapping.get(get_from),
            headers=headers,
            output="json",
        )
        return Item(**response)

    @staticmethod
    def __is_list_of(obj, of_: Any):
        return isinstance(obj, list) & all(isinstance(item, of_) for item in obj)

    @staticmethod
    def __from_econ_items(items: dict | list[dict], bulk: bool) -> ItemObjects:
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
