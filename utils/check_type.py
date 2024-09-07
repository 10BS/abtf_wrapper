class CheckType:
    @staticmethod
    def is_list_of_dicts(obj):
        return isinstance(obj, list) & all(isinstance(item, dict) for item in obj)
