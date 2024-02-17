import argparse
import logging
import shutil
from argparse import RawTextHelpFormatter
from pathlib import Path
from typing import Any, Tuple, Union

from .analyze import AttributeNameValidator, get_extra_catalog
from .config import (
    ATTRIBUTE_NAMING_GUIDELINES_AND_ANALYSIS_REPORT_USAGE_HTML_PATH,
    CATALOG_JSON_PATH, CATALOG_XLSX_PATH)
from .utilities import iter_csv_files


def analyze_entity(
    column_names_file_path: Path,
    catalog_document_path: Union[str, Path] = CATALOG_JSON_PATH,
    extra_class_word_abbreviations: Tuple = (),
    extra_acronyms: Tuple = (),
    write_to_text_files: bool = False,
) -> None:
    attribute_name_validator: AttributeNameValidator = AttributeNameValidator(
        column_names_file_path,
        catalog_document_path,
        extra_class_word_abbreviations,
        extra_acronyms,
        write_to_text_files,
    )
    attribute_name_validator.analyze_entity()
    attribute_name_validator.save_reports()


def analyze_entities(
    column_names_folder_path: Path,
    catalog_document_path: Union[str, Path] = CATALOG_JSON_PATH,
    extra_class_word_abbreviations: Tuple = (),
    extra_acronyms: Tuple = (),
    write_to_text_files: bool = False,
) -> None:
    logging.debug(f"Analyze Objects at {column_names_folder_path}")
    for column_names_file_path in iter_csv_files(column_names_folder_path):
        analyze_entity(
            column_names_file_path,
            catalog_document_path,
            extra_class_word_abbreviations,
            extra_acronyms,
            write_to_text_files,
        )


class _CustomArgumentParser(argparse.ArgumentParser):
    def __init__(self, prog: str, description: str, formatter_class: Any):
        super().__init__(
            prog=prog, description=description, formatter_class=formatter_class
        )


def copy_documentation() -> None:
    reports_directory: Path = Path().absolute().joinpath("reports")
    reports_directory.mkdir(parents=True, exist_ok=True)

    shutil.copy(
        ATTRIBUTE_NAMING_GUIDELINES_AND_ANALYSIS_REPORT_USAGE_HTML_PATH,
        reports_directory.joinpath(
            "ATTRIBUTE_NAMING_GUIDELINES_AND_ANALYSIS_REPORT_USAGE.html"
        ),
    )
    shutil.copy(CATALOG_XLSX_PATH, reports_directory.joinpath("CATALOG.xlsx"))


def main() -> None:
    copy_documentation()
    parser: _CustomArgumentParser = _CustomArgumentParser(
        prog="attribute-name-validator",
        formatter_class=RawTextHelpFormatter,
        description=(
            "This command generates report on naming analysis from either "
            "a list of column name files in a folder, \n"
            "or a given column names file, by looking up the words "
            "used to the column names in a local Abbreviation catalog \n "
            "that comes with the installation of package. On the"
            " execution of this command, you will also have a reports \n"
            "folder created with CATALOG.xlsx and "
            "COLUMN_NAMING_GUIDELINES_AND_ANALYSIS_REPORT_"
            "USAGE.html files, \n"
            "which have more information related to the working of the "
            "tool \n\n\n"
            "To add a set of Class Words Abbreviations and Acronyms, as "
            "exceptions beyond current enterprise guidelines\n"
            "create anv.ini file and add exceptions under respective "
            "sections, as shown below \n\n\n"
            "[additional-catalog]\n"
            "acronyms = LOB\n"
            "class-word-abbreviations = IN, IN3, CM3, LB\n"
        ),
    )
    parser.add_argument(
        "-l",
        "--log",
        action="store_const",
        const=True,
        default=False,
        help="This flag, if present, shows logs of execution in sys.stdout.",
    )
    parser.add_argument(
        "--write-to-text-files",
        "-wttf",
        action="store_const",
        const=True,
        default=False,
        help=(
            "This flag, if present, also creates text files of reports "
            "under their respective entity specific folder.\n\n"
        ),
    )
    parser.add_argument(
        "target_path",
        help="Path to file with column names or folder with "
        "column name files to analyze",
    )
    namespace: argparse.Namespace = parser.parse_args()
    if namespace.log:
        logging.basicConfig(level=logging.NOTSET)

    # load extra catalog
    catalog: Any = get_extra_catalog()

    path = Path(namespace.target_path)
    if path.is_dir():
        analyze_entities(
            column_names_folder_path=path,
            extra_class_word_abbreviations=(
                catalog.additional_class_word_abbreviations
            ),
            extra_acronyms=catalog.additional_acronyms,
            write_to_text_files=bool(namespace.write_to_text_files),
        )
    else:
        analyze_entity(
            column_names_file_path=path,
            extra_class_word_abbreviations=(
                catalog.additional_class_word_abbreviations
            ),
            extra_acronyms=catalog.additional_acronyms,
            write_to_text_files=bool(namespace.write_to_text_files),
        )


if __name__ == "__main__":
    main()
