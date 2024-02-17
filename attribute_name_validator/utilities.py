import csv
import re
from pathlib import Path
from typing import IO, Generator, Tuple


def iter_csv_files(folder: Path) -> Generator:
    return folder.glob("*.csv")


def iter_column_names(column_names_file_path: Path) -> Generator:
    """
    This function supports iteration of columns for any combination of
    following variations in a text file
    * multiple rows of column names
    * multiple column names in a row
    * leading and trailing spaces
    * convert spaces between names into list of columns
    """
    statement: str
    columns_io: IO[str]
    with column_names_file_path.open(
        mode="r", encoding="utf-8-sig"
    ) as columns_io:
        csv_reader = csv.reader(columns_io, delimiter=",")
        for row in csv_reader:
            for element in row:
                units = re.split(r"\s+", element.strip())
                for unit in units:
                    yield unit


def sanitize_ini(data: str) -> Tuple[str, ...]:
    # remove white spaces and return words
    pattern = re.compile(r"\s+")
    data = re.sub(pattern, "", data)
    return tuple(data.split(","))
