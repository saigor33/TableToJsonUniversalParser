from Configuration import FieldValueType, ReferenceType
from RowToJsonConverter.Node import Node

FeatureNodeExample: Node = Node(None, None, [
    # field values
    Node("str_field_name", None, [Node(FieldValueType.String, 'text', None)]),
    Node("num_field_name", None, [Node(FieldValueType.Number, '28', None)]),
    Node("bool_field_name", None, [Node(FieldValueType.Bool, 'true', None)]),
    Node("null_field_name", None, [Node(FieldValueType.Null, 'null', None)]),

    # object
    Node("obj_field_name", None, []),
    Node("obj_field_name", None, [
        Node("str_field_name", None, [Node(FieldValueType.String, 'text', None)])
    ]),

    # array
    Node("arr_field_name", ReferenceType.Array, [
        Node(None, None, [Node(FieldValueType.String, "text1", None)]),
        Node(None, None, [Node(FieldValueType.String, "text2", None)])
    ]),

    # array with objects
    Node("arr_field_name2", ReferenceType.Array, [
        Node(None, None, [
            Node("field1", None, [
                Node("field", None, [Node(FieldValueType.String, 'text', None)])
            ]),
            Node("field2", None, [
                Node("field", None, [Node(FieldValueType.String, 'text', None)])
            ]),
        ]),
        Node(None, None, [
            Node("field1", None, [
                Node("field", None, [Node(FieldValueType.String, 'text', None)])
            ]),
            Node("field2", None, [
                Node("field", None, [Node(FieldValueType.String, 'text', None)])
            ]),
        ]),
    ]),
])
