"""
This script parses '../CATALOG.xlsx' and outputs a catalog
document to '../attribute_name_validator/catalog.json'.
"""

import shutil
import sob
import os
from dataclasses import dataclass  # type: ignore
from itertools import islice
from collections import namedtuple
from openpyxl import Workbook, load_workbook  # type: ignore
from openpyxl.cell import Cell  # type: ignore
from typing import Iterable, Tuple, Type, Dict, Any
from pathlib import Path
from attribute_name_validator import model
from attribute_name_validator.config import (
    CATALOG_JSON_PATH,
    CATALOG_XLSX_PATH,
    ATTRIBUTE_NAMING_GUIDELINES_AND_ANALYSIS_REPORT_USAGE_HTML_PATH,
)

PROJECT_PATH: Path = Path(__file__).absolute().parent.parent
CATALOG_XLSX: str = str(PROJECT_PATH.joinpath("CATALOG.xlsx"))
TESTS_CATALOG_PATH: str = str(
    PROJECT_PATH.joinpath(
        "tests",
        "catalog.json",
    )
)
ATTRIBUTE_NAMING_GUIDELINES_AND_ANALYSIS_REPORT_USAGE_MD_PATH: Path = (
    PROJECT_PATH.joinpath(  # noqa
        "documentation/ATTRIBUTE_NAMING_"
        "GUIDELINES_AND_ANALYSIS_REPORT_USAGE.md"
    )
)


@dataclass
class ClassWord:
    abbreviation: str
    class_word: str
    sample_usage: str
    when_to_use: str


@dataclass
class Acronym:
    acronym: str
    phrase: str


@dataclass
class Aggregate:
    acronym: str
    phrase: str
    sample_usage: str
    when_to_use: str


def cast_named_tuple_as(value: Tuple, cls: type) -> Any:
    kwargs: Dict[str, Any] = {}
    field_name: str
    field_value: Any
    for field_name in cls.__dataclass_fields__:  # type: ignore
        field_value = getattr(value, field_name)
        if isinstance(field_value, str):
            field_value = field_value.strip()
            if not field_value:
                field_value = None
        kwargs[field_name] = field_value
    return cls(**kwargs)


class CatalogTables:
    """
    This class reads a catalog Excel workbook,
    validates the content matches the expected input, and exposes
    the tables contained within as instances of dataclasses declared
    within this module.

    Initialization Parameters:

    - workbook_path (str)
    """

    def __init__(self, workbook_path: str = CATALOG_XLSX) -> None:
        self.workbook: Workbook = load_workbook(workbook_path)

    def _iter_worksheet_rows(
        self, worksheet_name: str, cls: type
    ) -> Iterable[Tuple]:
        rows: Iterable[Iterable[Cell]] = iter(  # type: ignore
            self.workbook[worksheet_name]
        )
        cell: Cell
        column_names: Tuple[str, ...] = tuple(
            filter(
                None,
                map(
                    lambda cell: (
                        None if cell.value is None else cell.value.lower()
                    ),
                    next(rows),  # type: ignore
                ),
            )
        )
        length: int = len(column_names)
        Row: Type[tuple] = namedtuple(  # type: ignore
            sob.utilities.string.class_name(worksheet_name), column_names
        )
        for row in rows:
            yield cast_named_tuple_as(
                Row(*map(lambda cell: cell.value, islice(row, length))), cls
            )

    @property
    def class_word(self) -> Iterable[ClassWord]:
        yield from self._iter_worksheet_rows(  # type: ignore
            "CLASS_WORD", ClassWord
        )

    @property
    def acronym(self) -> Iterable[Acronym]:
        yield from self._iter_worksheet_rows(  # type: ignore
            "ACRONYM", Acronym
        )

    @property
    def aggregate(self) -> Iterable[Aggregate]:
        yield from self._iter_worksheet_rows(  # type: ignore
            "AGGREGATE", Aggregate
        )


class Mapper:
    """
    This class translates the contents of a catalog
    Excel workbook into a JSON document for distribution with
    `attribute-name-validator`.

    Initialization Parameters:

    - workbook_path (str)
    """

    def __init__(self, workbook_path: str = CATALOG_XLSX) -> None:
        self.catalog_tables: CatalogTables = CatalogTables(workbook_path)

    def _get_class_word_abbreviations(
        self,
    ) -> model.ClassWordAbbreviations:
        class_words: model.ClassWordAbbreviations = (
            model.ClassWordAbbreviations()
        )
        row: ClassWord
        for row in self.catalog_tables.class_word:
            if row.abbreviation:
                assert row.class_word
                class_words[row.abbreviation.upper()] = (
                    model.ClassWordAbbreviation(
                        abbreviation=row.abbreviation.upper(),
                        class_word=row.class_word.upper(),
                        sample_usage=row.sample_usage,
                        when_to_use=row.when_to_use,
                    )
                )
        return class_words

    def _get_class_words(
        self,
    ) -> model.ClassWords:
        class_words: model.ClassWords = model.ClassWords()
        row: ClassWord
        for row in self.catalog_tables.class_word:
            if row.class_word:
                assert row.class_word
                class_words[row.class_word.upper()] = dict()
        return class_words

    def _get_acronyms(
        self,
    ) -> model.Acronyms:
        acronyms: model.Acronyms = model.Acronyms()
        row: Acronym
        for row in self.catalog_tables.acronym:
            if row.acronym and row.phrase:
                if row.acronym not in acronyms:
                    acronyms[row.acronym] = model.Phrases()
                acronyms[row.acronym].append(row.phrase)
        return acronyms

    def _get_aggregates(
        self,
    ) -> model.Aggregates:
        aggregates: model.Aggregates = model.Aggregates()
        row: Aggregate
        for row in self.catalog_tables.aggregate:
            if row.acronym:
                aggregates[row.acronym] = model.Aggregate(
                    phrase=row.phrase,
                    sample_usage=row.sample_usage,
                    when_to_use=row.when_to_use,
                )
        return aggregates

    def get_catalog_document(self) -> model.CatalogDocument:
        document: model.CatalogDocument = model.CatalogDocument(
            class_words=self._get_class_words(),
            class_word_abbreviations=self._get_class_word_abbreviations(),
            acronyms=self._get_acronyms(),
            aggregates=self._get_aggregates(),
        )
        return document

    def update_catalog_json(self) -> None:
        """
        This method updates catalog.json (if any changes have been made)
        """
        catalog_document: model.CatalogDocument = self.get_catalog_document()
        print(f"Updating {CATALOG_JSON_PATH}")
        with open(CATALOG_JSON_PATH, "w") as catalog_json_io:
            catalog_json_io.write(
                f"{sob.model.serialize(catalog_document, indent=4)}\n"
            )


def update_column_naming_guidelines() -> None:
    """
    Upgrade column naming guidelines in package, to avoid editing it twice
     and return `None` if successful (otherwise return the error).
    """
    command: str = (
        f"cat {ATTRIBUTE_NAMING_GUIDELINES_AND_ANALYSIS_REPORT_USAGE_MD_PATH}"
        f"|marko "
        f">{ATTRIBUTE_NAMING_GUIDELINES_AND_ANALYSIS_REPORT_USAGE_HTML_PATH}"
    )
    os.system(command)


def main() -> None:
    Mapper().update_catalog_json()
    # Also copy xlsx and html files to be available with package
    # for distribution and end user consumption.
    shutil.copy2(CATALOG_XLSX, CATALOG_XLSX_PATH)
    update_column_naming_guidelines()


if __name__ == "__main__":
    main()
