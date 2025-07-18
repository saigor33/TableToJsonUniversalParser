from typing import Optional


class Row:
    def __init__(self,
                 visible_number: int,
                 link_id: str,
                 field_name: str,
                 field_value_type: str,
                 field_value: str,
                 alias_func_arg_value: str,
                 anonym_args: Optional[dict[str, str]]
                 ):
        self.visible_number = visible_number
        self.link_id = link_id
        self.field_name = field_name
        self.field_value_type = field_value_type
        self.field_value = field_value
        self.alias_func_arg_value = alias_func_arg_value
        self.anonym_args = anonym_args
