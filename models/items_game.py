from datetime import datetime
from typing import Optional, ClassVar

from pydantic import BaseModel, Field


class Rarity(BaseModel):
    value: int
    loc_key: str
    loc_key_weapon: str
    color: str
    loot_list: Optional[str]
    drop_sound: Optional[str]
    next_rarity: Optional[str]


class ConditionLogic(BaseModel):
    type: str
    value: Optional[str] = None
    player_key: Optional[str] = None
    get_player: Optional[str] = None
    is_owner: Optional[int] = None
    team_key: Optional[str] = None
    team_requirement: Optional[int] = None
    distance_check_type: Optional[int] = None
    distance_to_check: Optional[int] = None
    key_to_lookup: Optional[str] = None


class Quest(BaseModel):
    name: str
    condition_logic: dict[str, dict[str, ConditionLogic]]
    type: str
    event_name: Optional[str] = None
    score_key_name: Optional[str] = None


class QuestObjectiveConditions(BaseModel):
    success: bool
    value: dict[str, Quest]


class CardType(BaseModel):
    value: int
    loc_key: str
    ui: str


class ItemCollection(BaseModel):
    name: str
    description: str
    is_reference_collection: int
    items: dict[str, int | dict[str, int]]


class Operation(BaseModel):
    name: str
    operation_start_date: datetime
    stop_adding_to_queue_date: datetime
    stop_giving_to_player_date: datetime
    contracts_end_date: datetime
    operation_loot_list: str = Field(alias="operation_lootlist")
    is_campaign: Optional[int] = None
    max_drop_count: Optional[int] = None
    uses_credits: Optional[int] = None


class CapabilityExt(BaseModel, extra="allow"):
    can_craft_count: ClassVar[bool]
    paintable: ClassVar[bool]


class Tool(BaseModel):
    type: str
    usage_capabilities: dict[str, bool]
    restriction: str


class Tag(BaseModel, extra="allow"):
    can_deal_damage: ClassVar[bool]
    can_deal_mvm_penetration_damage: ClassVar[bool]
    can_deal_long_distance_damage: ClassVar[bool]


class PlayerBodyGroup(BaseModel, extra="allow"):
    hat: ClassVar[bool]
    head: ClassVar[bool]
    headphones: ClassVar[bool]
    grenades: ClassVar[bool]
    dogtags: ClassVar[bool]
    backpack: ClassVar[bool]
    shoes: ClassVar[bool]
    shoes_socks: ClassVar[bool]


class AdditionalHiddenBodyGroup(BaseModel, extra="allow"):
    hat: ClassVar[bool]
    head: ClassVar[bool]
    headphones: ClassVar[bool]
    grenades: ClassVar[bool]
    dogtags: ClassVar[bool]


class Style(BaseModel):
    name: str
    model_player: str
    additional_hidden_bodygroups: AdditionalHiddenBodyGroup
    model_player_per_class: dict[str, str]
    skin_red: bool
    skin_blu: bool


class Visuals(BaseModel):
    player_bodygroups: PlayerBodyGroup
    styles: dict[int, Style]
    custom_particlesystem: dict[str, str]
    sound_deploy: str


class StaticAttr(BaseModel):
    set_supply_crate_series: int = Field(alias="set supply crate series")
    hide_crate_series_number: bool = Field(alias="hide crate series numbers")
    decoded_by_item_def_index: int = Field(alias="decoded by itemdefindex")
    weapon_allow_inspect: bool
    item_style_override: bool = Field(alias="item style override")
    is_winter_case: bool = Field(alias="is winter case")
    is_marketable: bool = Field(alias="is marketable")
    is_commodity: bool = Field(alias="is commodity")
    kill_eater_score_type: int = Field(alias="kill eater score type")
    kill_eater_score_type_2: int = Field(alias="kill eater score type 2")
    kill_eater_score_type_3: int = Field(alias="kill eater score type 3")
    cannot_trade: bool = Field(alias="cannot trade")
    is_operation_pass: bool
    style_changes_on_strange_level: int = Field(alias="style changes on strange level")
    cannot_restore: bool = Field(alias="cannot restore")
    cannot_giftwrap: bool = Field(alias="cannot giftwrap")
    always_transmit_so: bool
    never_craftable: bool = Field(alias="never craftable")
    deactive_date: int = Field(alias="deactive date")
    paintkit_proto_def_index: int
    has_team_color_paintkit: bool
    limited_quantity_item: bool = Field(alias="limited quantity item")
    is_giger_counter: bool = Field(alias="is giger counter")
    min_viewmodel_offset: list[int]
    inspect_viewmodel_offset: list[int]
    item_meter_charge_type: int
    item_meter_charge_rate: int
    meter_label: str
    mult_player_movespeed_active: float
    mod_maxhealth_drain_rate: float
    energy_weapon_no_ammo: bool
    energy_weapon_charged_shot: bool
    energy_weapon_no_hurt_building: bool
    crits_become_minicrits: bool
    crit_mod_disabled: bool
    always_tradable: bool
    tool_target_item: int = Field(alias="tool target item")


class ItemsGameItems(BaseModel, extra="allow"):
    name: str
    first_sale_date: ClassVar[datetime]
    prefab: ClassVar[str]
    baseitem: ClassVar[int]
    capabilities: ClassVar[CapabilityExt]
    equip_regions: ClassVar[dict[str, int]]
    propername: ClassVar[bool]
    min_ilevel: ClassVar[int]
    max_ilevel: ClassVar[int]
    hidden: ClassVar[str]
    inspect_panel_dist: ClassVar[int]
    item_name: ClassVar[str]
    item_type_name: ClassVar[str]
    item_slot: ClassVar[str]
    item_quality: ClassVar[str]
    image_inventory: ClassVar[str]
    image_inventory_size_w: ClassVar[int]
    image_inventory_size_h: ClassVar[int]
    craft_class: ClassVar[str]
    craft_material_type: ClassVar[str]
    player_model: ClassVar[str] = Field(alias="model_player")
    attach_to_hands: ClassVar[int]
    drop_type: ClassVar[str]
    used_by_classes: ClassVar[dict[str, bool]]
    mouse_pressed_sound: ClassVar[str]
    drop_sound: ClassVar[str]
    tags: ClassVar[Tag]
    ad_text: ClassVar[str]
    default_skin: ClassVar[int]
    static_attrs: ClassVar[StaticAttr]
    xifier_class_remap: ClassVar[str]
