import json
from typing import Literal, Optional

from models.item_name_sku import ItemNames, ItemSkus
from models.item_object import ItemObjects
from models.schema import (
    ItemOrigins,
    ItemAttributes,
    ItemSets,
    SchemaProperty,
    ItemGrades,
    GenericResponseModel,
)
from utils import request
from utils.check_type import CheckType


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
            "craftWeaponsByClass/",
        ],
        class_char: Optional[
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
        ] = None,
    ) -> SchemaProperty:
        headers = {
            "accept": "*/*",
        }
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
        return SchemaProperty(values=response)

    @staticmethod
    def get_name(
        items: str | dict | list[str | dict], get_from: Literal["item_object", "sku"]
    ) -> ItemNames:
        bulk: bool = True if isinstance(items, list) else False
        headers = {
            "accept": "*/*",
        }
        if bulk:
            headers["Content-Type"] = "application/json"
        method_mapping = {
            "item_object": "fromItemObjectBulk" if bulk else f"fromItemObject",
            "sku": (
                "fromSkuBulk"
                if bulk & CheckType.is_list_of(items, str)
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
        headers = {
            "accept": "*/*",
        }
        if bulk:
            headers["Content-Type"] = "application/json"
        method_mapping = {
            "item_object": "fromItemObjectBulk" if bulk else f"fromItemObject",
            "name": (
                "fromNameBulk"
                if bulk & CheckType.is_list_of(items, str)
                else f"fromName/{items}"
            ),
            "econ_item": (
                "fromEconItemBulk"
                if bulk & CheckType.is_list_of(items, dict)
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
        by_: Optional[int | str] = None,
        get_from: Optional[Literal["def_index", "name", "sku"]] = None,
        get_grades: Optional[bool] = None,
        grades_v: Optional[Literal[1, 2]] = None,
    ) -> GenericResponseModel:
        if get_grades:
            return AutobotTF.__get_grades(grades_v)
        headers = {
            "accept": "*/*",
        }
        method_mapping = {
            "def_index": f"fromDefindex/{by_}",
            "name": f"fromName/{by_}",
            "sku": f"fromSku/{by_}",
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
    def __get_grades(v_: Literal[1, 2]) -> ItemGrades:
        headers = {
            "accept": "*/*",
        }
        response = request.make_request(
            method="GET",
            base_url="https://schema.autobot.tf/",
            url=f"getItemGrade/v{v_}",
            headers=headers,
            output="json",
        )
        return ItemGrades(**response)
