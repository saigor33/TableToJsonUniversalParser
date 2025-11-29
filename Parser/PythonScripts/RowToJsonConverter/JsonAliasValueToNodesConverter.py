import json
from typing import Optional
from Configuration import FieldValueType, ReferenceType
from RowToJsonConverter.Node import Node


def convert(alias_value: str) -> Node:
    alias_value_field_name = "aliasField"
    json_text = f'{{"{alias_value_field_name}":{alias_value}}}'
    json_read_result = json.loads(json_text)

    return __RecursiveConvert(None, json_read_result[alias_value_field_name])


def __RecursiveConvert(field_name: Optional[str], json_value) -> Node:
    if json_value is None:
        return Node(field_name, None, [Node(FieldValueType.Null, json_value, None)])

    field_value_type = type(json_value)
    if field_value_type == dict:
        return Node(field_name, None, [__RecursiveConvert(k, v) for k, v in json_value.items()])
    elif field_value_type == list:
        return Node(field_name, ReferenceType.Array, [__RecursiveConvert(None, json_item) for json_item in json_value])
    elif field_value_type == str:
        return Node(field_name, None, [Node(FieldValueType.String, json_value, None)])
    elif field_value_type == int:
        return Node(field_name, None, [Node(FieldValueType.Number, json_value, None)])
    elif field_value_type == float:
        return Node(field_name, None, [Node(FieldValueType.Number, json_value, None)])
    elif field_value_type == bool:
        return Node(field_name, None, [Node(FieldValueType.Bool, json_value, None)])
    else:
        raise Exception(f'Unhandled json type="{field_value_type}" json_value={json_value}')
