from pydantic import BaseModel


class DefIndexes(BaseModel):
    values: dict[int, str]


class Qualities(BaseModel):
    values: dict[str, int]


class Killstreaks(BaseModel):
    values: dict[int | str, str | int]


class Effects(BaseModel):
    values: dict[str, int]


class Paintkits(BaseModel):
    values: dict[str, int]


class Wears(BaseModel):
    values: dict[int | str, str | int]


class CrateSeries(BaseModel):
    values: dict[int, int]


class Paints(BaseModel):
    values: dict[str, int]


class StrangeParts(BaseModel):
    values: dict[str, str]


class CraftWeapons(BaseModel):
    values: list[str]


class UncraftWeapons(BaseModel):
    values: list[str]


class CraftWeaponsByClass(BaseModel):
    values: list[str]
