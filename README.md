# attribute-name-validator
[![test](https://github.com/siddartham/attribute-name-validator/actions/workflows/test.yml/badge.svg)](https://github.com/siddartham/attribute-name-validator/actions/workflows/test.yml)
[![distribute](https://github.com/siddartham/attribute-name-validator/actions/workflows/distribute.yml/badge.svg)](https://github.com/siddartham/attribute-name-validator/actions/workflows/distribute.yml)

This pacakge provides a CLI for column name analysis. It also acts as library for catalog of approved abbreviations and codified column naming rules.

The CLI, when provided a text file with column names used in the physical data layer for a given entity,
generates a report, based on Data Modeling and Naming Standards defined within this repository.


See [ATTRIBUTE NAMING GUIDELINES AND ANALYSIS REPORT USAGE](documentation/ATTRIBUTE_NAMING_GUIDELINES_AND_ANALYSIS_REPORT_USAGE.md) for further
information pertaining to the issues faced during the naming of columns and how this package
can be used to get feed back on column names, and help standardize column naming.

See [CONTRIBUTING.md](documentation/CONTRIBUTING.md) for information pertaining to
development of this package.


## Install

Install the package using pip from github

```shell script
pip3 install git+https://github.com/siddartham/attribute-name-validator.git
```

## Usage

Report of each execution has the catalog of class words, acronyms included. This way, we can see the source data set, based on which reports were produced and lookup approved acronyms.

### Work Flow
![Screenshot](documentation/AttributeNameValidator.png)

```shell

$ anv -h
usage: attribute-name-validator [-h] [-l] [--write-to-text-files] target_path

This command generates report on naming analysis from either a list of column name files in a folder,
or a given column names file, by looking up the words used to the column names in a local Abbreviation catalog
 that comes with the installation of package. On the execution of this command, you will also have a reports
folder created with CATALOG.xlsx and COLUMN_NAMING_GUIDELINES_AND_ANALYSIS_REPORT_USAGE.html files,
which have more information related to the working of the tool

To add a set of Class Words Abbreviations and Acronyms, as exceptions beyond current enterprise guidelines
create ncna.ini file and add exceptions under respective sections, as shown below

[additional-catalog]
acronyms = LOB
class-word-abbreviations = IN, IN3, CM3, LB

positional arguments:
  target_path           Path to file with column names or folder with column name files to analyze

optional arguments:
  -h, --help            show this help message and exit
  -l, --log             This flag, if present, shows logs of execution in sys.stdout.
  --write-to-text-files, -wttf
                        This flag, if present, also creates text files of reports under their respective entity specific folder.

```
Provide a relative/absolute path to file with the list of column names to be used for the entity, with each column in a new line.

```shell
$ anv <PATH_TO_<ENTITY_NAME>>
$ ls reports/
ATTRIBUTE_NAMING_GUIDELINES_AND_REPORT_USAGE.html        CATALOG.xlsx                            TABLE_NEW_REPORT.xlsx
$ anv <PATH_TO_ENTITY_FOLDER>
$ ls reports/
ATTRIBUTE_NAMING_GUIDELINES_AND_REPORT_USAGE.html       ENTITY_1_REPORT.xlsx                                    ENTITY_3
CATALOG.xlsx                                            ENTITY_2                                                ENTITY_3_REPORT.xlsx
ENTITY_1                                                ENTITY_2_REPORT.xlsx
```

## TASK LOG
See [TASKLOG.md](documentation/TASKLOG.md) for information pertaining to the development history of the package and
the next set of tasks.
