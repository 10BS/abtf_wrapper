from typing import Any


class CheckType:
    @staticmethod
    def is_list_of(obj, of_: Any):
        return isinstance(obj, list) & all(isinstance(item, of_) for item in obj)
