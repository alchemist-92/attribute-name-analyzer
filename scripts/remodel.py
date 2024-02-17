import sob
from oapi.oas import model
from oapi.model import Module  # noqa
from pathlib import Path

_PROJECT_PATH: Path = Path(__file__).absolute().parent.parent
OPENAPI_JSON: str = str(_PROJECT_PATH.joinpath("openapi.json"))
MODEL_PY: str = str(
    _PROJECT_PATH.joinpath("attribute_name_validator", "model.py")
)


def update_openapi() -> model.OpenAPI:
    openapi: model.OpenAPI = model.OpenAPI(
        openapi="3.1.0",
        info=model.Info(
            title="Attribute Name Analyzer",
            description=(
                "This document describes schemas for the input to, output "
                "from the attribute-name-validator(anv) "
                "package. "
                "No `paths` are defined in this document because this "
                "application is not a REST API, it is a python library and "
                "command line interface (CLI)."
            ),
        ),
        components=model.Components(
            schemas=model.Schemas(
                [
                    (
                        "catalog_document",
                        model.Schema(
                            description="The root document for the catalog ",
                            type_="object",
                            properties=model.Properties(
                                [
                                    (
                                        "class_word_abbreviations",
                                        model.Reference(
                                            ref=(
                                                "#/components/schemas/"
                                                "class_word_abbreviations"
                                            )
                                        ),
                                    ),
                                    (
                                        "class_words",
                                        model.Reference(
                                            ref=(
                                                "#/components/schemas/"
                                                "class_words"
                                            )
                                        ),
                                    ),
                                    (
                                        "acronyms",
                                        model.Reference(
                                            ref=(
                                                "#/components/schemas/"
                                                "acronyms"
                                            )
                                        ),
                                    ),
                                    (
                                        "aggregates",
                                        model.Reference(
                                            ref=(
                                                "#/components/schemas/"
                                                "aggregates"
                                            )
                                        ),
                                    ),
                                ]
                            ),
                        ),
                    ),
                    (
                        "class_words",
                        model.Schema(
                            type_="object",
                            description="A collection of  class words.",
                            additional_properties=model.Reference(
                                ref="#/components/schemas/class_word"
                            ),
                        ),
                    ),
                    (
                        "class_word",
                        model.Schema(
                            type_="object",
                            description="Information about a class word.",
                            properties=model.Properties([]),
                        ),
                    ),
                    (
                        "class_word_abbreviations",
                        model.Schema(
                            type_="object",
                            description=(
                                "A dictionary mapping abbreviated class words "
                                "to class words and usage information about "
                                "each."
                            ),
                            additional_properties=model.Reference(
                                ref="#/components/schemas/class_word_"
                                "abbreviation"
                            ),
                        ),
                    ),
                    (
                        "class_word_abbreviation",
                        model.Schema(
                            type_="object",
                            description="Information about a class word.",
                            properties=model.Properties(
                                [
                                    (
                                        "abbreviation",
                                        model.Schema(type_="string"),
                                    ),
                                    (
                                        "class_word",
                                        model.Schema(type_="string"),
                                    ),
                                    (
                                        "sample_usage",
                                        model.Schema(type_="string"),
                                    ),
                                    (
                                        "when_to_use",
                                        model.Schema(
                                            type_="string",
                                        ),
                                    ),
                                ]
                            ),
                        ),
                    ),
                    (
                        "acronyms",
                        model.Schema(
                            type_="object",
                            description=(
                                "A mapping of ACRONYMS to a list of phrases "
                                "which they are approved to be used for."
                            ),
                            additional_properties=model.Reference(
                                ref="#/components/schemas/phrases"
                            ),
                        ),
                    ),
                    (
                        "phrases",
                        model.Schema(
                            type_="array",
                            description=(
                                "One or more phrases acronym to be used for"
                            ),
                            items=model.Schema(type_="string"),
                        ),
                    ),
                    (
                        "aggregates",
                        model.Schema(
                            type_="object",
                            description=(
                                "A mapping of aggregate acronyms to its usage"
                            ),
                            additional_properties=model.Reference(
                                ref="#/components/schemas/aggregate"
                            ),
                        ),
                    ),
                    (
                        "aggregate",
                        model.Schema(
                            type_="object",
                            description=(
                                "One or more phrases acronym to be used for"
                            ),
                            properties=model.Properties(
                                [
                                    (
                                        "phrase",
                                        model.Schema(type_="string"),
                                    ),
                                    (
                                        "sample_usage",
                                        model.Schema(type_="string"),
                                    ),
                                    (
                                        "when_to_use",
                                        model.Schema(type_="string"),
                                    ),
                                ]
                            ),
                        ),
                    ),
                    (
                        "class_word_analysis_report",
                        model.Schema(
                            type_="object",
                            description=(
                                "A mapping of ACRONYMS to a list of phrases "
                                "which they are approved to be used for."
                            ),
                            additional_properties=model.Reference(
                                ref="#/components/schemas/column_name_class_"
                                "word_analysis"
                            ),
                        ),
                    ),
                    (
                        "column_name_class_word_analysis",
                        model.Schema(
                            type_="array",
                            description="Class word analysis of "
                            "an column name.",
                            items=model.Reference(
                                ref="#/components/schemas/column_"
                                "name_class_word_analysis_unit"
                            ),
                        ),
                    ),
                    (
                        "used_abbreviations",
                        model.Schema(
                            type_="object",
                            description=(
                                "This object records data pertaining to all "
                                "instances of the usage of all approved "
                                "abbreviations, and the abbreviation's "
                                "approved usages. This is for ensuring "
                                "they are used only for approved usages."
                            ),
                            additional_properties=model.Reference(
                                ref="#/components/schemas/used_abbreviation"
                            ),
                        ),
                    ),
                    (
                        "used_abbreviation",
                        model.Schema(
                            type_="object",
                            description=(
                                "This object records data pertaining to all "
                                "instances of the usage of an approved "
                                "abbreviation, and the abbreviation's "
                                "approved usages "
                            ),
                            properties=model.Properties(
                                [
                                    (
                                        "column_names",
                                        model.Schema(
                                            type_="array",
                                            items=model.Schema(type_="string"),
                                        ),
                                    ),
                                    (
                                        "allowed_usages",
                                        model.Schema(
                                            type_="array",
                                            items=model.Schema(type_="string"),
                                        ),
                                    ),
                                ]
                            ),
                        ),
                    ),
                    (
                        "column_name_class_word_analysis_unit",
                        model.Schema(
                            type_="object",
                            description="Class Word Analysis Instance",
                            properties=model.Properties(
                                [
                                    (
                                        "column_name",
                                        model.Schema(
                                            type_="string",
                                        ),
                                    ),
                                    (
                                        "word",
                                        model.Schema(
                                            type_="string",
                                        ),
                                    ),
                                    (
                                        "analysis",
                                        model.Schema(
                                            type_="string",
                                            enum=(
                                                "ABBREVIATED CLASS WORD IS "
                                                "USED IN THE MIDDLE",
                                                "FULL CLASS WORD IS USED IN "
                                                "THE MIDDLE",
                                                "FULL CLASS WORD IS USED AT "
                                                "THE END",
                                                "APPROVED ACRONYM IS USED AT "
                                                "THE END",
                                                "GENERIC WORD USED AT THE END",
                                                "ABBREVIATED CLASS WORD IS "
                                                "USED AT THE END",
                                                "CLASS WORD IS USED AS "
                                                "COLUMN NAME",
                                                "UNIT SPECIFIC CLASS WORD MAY "
                                                "BE NEEDED AT THE END",
                                                "AGGREGATE ACRONYM IS USED AT "
                                                "THE END",
                                                "AGGREGATE ACRONYM IS USED IN "
                                                "THE MIDDLE",
                                                "NO CLASS WORD IS USED IN "
                                                "THE NAME",
                                            ),
                                        ),
                                    ),
                                    (
                                        "class_word_rules_followed",
                                        model.Schema(
                                            type_="string",
                                            enum=(
                                                "YES",
                                                "NO",
                                                "MAY BE",
                                            ),
                                        ),
                                    ),
                                    (
                                        "additional_notes",
                                        model.Schema(
                                            type_="string",
                                        ),
                                    ),
                                    (
                                        "when_to_use",
                                        model.Schema(
                                            type_="string",
                                        ),
                                    ),
                                ]
                            ),
                        ),
                    ),
                ]
            )
        ),
    )
    with open(OPENAPI_JSON, "w") as openapi_io:
        openapi_io.write(sob.model.serialize(openapi, indent=4))
    return openapi


def main() -> None:
    openapi: model.OpenAPI = update_openapi()
    Module(openapi).save(MODEL_PY)


if __name__ == "__main__":
    main()
