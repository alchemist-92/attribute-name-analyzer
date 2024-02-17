from pathlib import Path

PACKAGE_ROOT: Path = Path(__file__).absolute().parent
ATTRIBUTE_NAMING_GUIDELINES_AND_ANALYSIS_REPORT_USAGE_HTML_PATH: Path = (
    PACKAGE_ROOT.joinpath(
        "ATTRIBUTE_NAMING_GUIDELINES_AND_ANALYSIS_REPORT_USAGE.html"
    )
)
CATALOG_JSON_PATH: Path = PACKAGE_ROOT.joinpath("catalog.json")
CATALOG_XLSX_PATH: Path = PACKAGE_ROOT.joinpath("CATALOG.xlsx")

OUTPUT_XLSX_COLUMN_DIMENSIONS = {
    "CLASS_WORD_ANALYSIS": [40, 17, 42, 26, 40],
    "FULL_WORDS_USED": [18],
    "APPROVED_ACRONYMS_USED": [15, 40, 40],
}

ADDITIONAL_QUALIFIER_NEEDED_CLASS_WORDS = {
    "TIME": "Is this a unit of measurement?, is it Days? - "
    "Months ? or is this meant to be a Timestamp/Tmst?",
    "TM": "Is this a unit of measurement?, is it Days? - "
    "Months ? or is this meant to be a Timestamp/Tmst?",
    "AMOUNT": "What is the currency denomination? USD? EUR?",
    "AMT": "What is the currency denomination? USD? EUR?",
    "PRICE": "What is the currency denomination? USD? EUR?",
    "PRC": "What is the currency denomination? USD? EUR?",
    "COST": "What is the currency denomination? USD? EUR?",
    "WEIGHT": "What is the unit of measurement? KG? LB?",
    "WT": "What is the unit of measurement? KG? LB?",
    "LENGTH": "What is the unit of measurement? M? CM? IN?",
    "LEN": "What is the unit of measurement? M? CM? IN?",
    "WIDTH": "What is the unit of measurement? M? CM? IN?",
    "WDTH": "What is the unit of measurement? M? CM? IN?",
    "HGTH": "What is the unit of measurement? M? CM? IN?",
    "HEIGHT": "What is the unit of measurement? M? CM? IN?",
    "AREA": "What is unit of measurement? KM2, M2, CM2, IN2?",
    "VOL": "What is the unit of measurement? M3? CM3? ",
    "VOLUME": "What is the unit of measurement? M3? CM3? ",
}
