from typing import Optional

from Sources.Configuration.Configs.DebugConfig import DebugConfig
from Sources.Configuration.Configs.ExcelSourceConfig import ExcelSourceConfig
from Sources.Configuration.Configs.GoogleSheetsSourceConfig import GoogleSheetsSourceConfig
from Sources.Configuration.Configs.ParsingFeatureConfig import ParsingFeatureConfig
from Sources.Configuration.Configs.SourceType import SourceType


class Config:
    def __init__(self,
                 padding_per_layer: str,
                 need_parse_json_alias: bool,
                 debug: DebugConfig,
                 selected_source_type: SourceType,
                 excel_source: ExcelSourceConfig,
                 google_sheets_source: GoogleSheetsSourceConfig,
                 parsing_features: dict[str, ParsingFeatureConfig],
                 json_aliases_file_paths: list[str]):
        self.padding_per_layer = padding_per_layer
        self.need_parse_json_alias = need_parse_json_alias
        self.debug = debug
        self.selected_source_type = selected_source_type
        self.excel_source = excel_source
        self.google_sheets_source = google_sheets_source
        self.parsing_features = parsing_features
        self.json_aliases_file_paths = json_aliases_file_paths
