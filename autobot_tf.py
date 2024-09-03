import json

from pydantic import Field

from models.abtf.schema import (
    ItemName,
    ItemOrigins,
    ItemAttributes,
    ItemSets
)
from utils import request


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
            headers=headers
        )
        with open("schema.json", "w", encoding="utf-8") as schema:
            json.dump(response.json(), schema, indent=4)

    @staticmethod
    def get_origins() -> ItemOrigins:
        headers = {
            "accept": "*/*",
        }
        response = request.make_request(
            method="GET",
            base_url="https://schema.autobot.tf/",
            url="raw/schema/originNames",
            headers=headers
        )
        data = ItemOrigins(**response.json())
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
            headers=headers
        )
        data = ItemAttributes(**response.json())
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
            headers=headers
        )
        data = ItemSets(**response.json())
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
