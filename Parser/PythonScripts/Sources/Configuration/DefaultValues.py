from Sources.Configuration.Configs.DebugConfig import DebugConfig

PaddingPerLayer: str = "    "
NeedParseJsonAliasValue: bool = True
Debug: DebugConfig = DebugConfig(need_print_benchmarks=False)
JsonAliasesFilePaths: list[str] = []
AnonymAliasFuncArgNameByColumnName: dict[str, str] = {}
