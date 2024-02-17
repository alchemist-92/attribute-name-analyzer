## TASK LOG
#### Code Quality
1. Make package Pythonic. - ONGOING
2. Fix Typing Issues - ONGOING
3. Look for ways to make tests happen in `tox`. - DONE
   1. Resolved dependency issues.
4. Remove code specific to generate test reports in `analyze` module by parameterizing it. - DONE
5. Move repeatedly used/package specific constants to `config.py` module. - DONE
6. Move logic unrelated to analysis from `analyze.py` to `utilities.py` module. - DONE
7. Change input catalog `CLASS_WORDS.csv` and `ACRONYMS.csv` to `CLASS_WORDS.xlsx` and `ACRONYMS.xlsx` for easier
maintenance. - DONE
8. **Decide on the package to be used to read xlsx sheets**. Going with `openpyxl` package for reading and writing xlsx files.
`openpyxl` is a lean library for reading, writing and formatting xlsx files, which is all we need. We are not doing
relatively expansive data manipulations to warrant `pandas` - a massive module with all kinds of data analysis and
manipulation tools, which includes reading and writing to excel. Since we use exclusively xlsx files, not csv or
other tabular data formats, and have fine control over the limited data in `CATALOG.xlsx` and outputs generated
`ENTITY_NAME_REPORT.xlsx`. [Incidentally pandas uses openpyxl as an extra
dependency to extend its functionality to read and write xlsx files](https://pandas.pydata.org/docs/getting_started/install.html#excel-files),
 but it doesn't expose `openpyxl` as dependency to be installed like `pip install pandas[openpyxl] `, thus would still face
installation errors, if we don't install `openpyxl` separately. This defeats the purpose of `pandas` for our use case. - DONE
9. Merge `CLASS_WORDS.xlsx` and `ACRONYMS.xlsx` source data sets, into a single file - `CATALOG.xlsx`. - DONE
10. Merge `class_words.json` and `acronyms.json` in `column_name_analyzer/` into a single file - `catalog.json`. - DONE
11. Change the process of the creation of `catalog.json`, and reading from `catalog.json` from
json dumping and loading into `serialization` and `deserialization`.
    1. To serialize and deserialize data, use `sob` package.
    2. The classes needed for serialization and deserialization can be auto-generated using `oapi`.
       1. Define schemas, in `OpenAPI` format for all the data structures used in loading the data from `CATALOG.xlsx`,
    3. Also write schemas for objects used to handle several kinds
       of analysis reports(`CLASS_WORD_ANALYSIS`, `LONG_FORM_WORD`, `USED_CATALOG`)
    4. It has several advantages:
       1. enables better control and validation of input data and report generation(like programmatically
       limiting use of possible outcomes in reports etc.)
       2. The object-oriented way to deal with the data, enables logic flow of naming rules, that is easier to follow,
       than referencing data in a dictionary with key strings.
       3. In the process of building the package, we tend to do a lot of refactoring, for the name and structure
       changes of objects as it is deemed appropriate with the latest understanding of the nature of the problem.
       We need that flexibility, else we will be tied
       to the naming decisions and structures of the object, made at the beginning.
          1. With the combination of the use of type hinting and auto-generation of class data structures,
          by just changing `OpenAPI` schema and running the `remodel` script, we can quickly refactor the codebase,
          auto-directed by `mypy` raised issues and IDE based plugins.
          2. With the alternative method of, reading catalog json data into a dictionary, it will be a humongous
          task to refactor, as only type hinting is supported to maintain the structure of dictionary.
       4. we may potentially need a lot more input objects to deal with all quirks in naming rules, as different sheets
       in `CATALOG.xlsx`, such as **`CLASS WORD EXCEPTION`** - which could be list of words which are allowed at the end
       of column name, but not class words such as _WTD, _MTD, _YTD, _4WK, _12WK etc, but at the same time expect a
       class word preceding it. This and more cases like this invite spaghetti code, if we write the entire
       rule book as a singular python script or hard to refactor object-oriented code, when we want to change names
       of properties and class names in schema, or change relation between objects.
12. Refactor `schema/remodel.py`, rest of the package to update class word related Class names in `column_name_analyzer/model.py` to be
consistent with class word abbreviation and class word. Right now, root_document.class_word to access class_word
abbreviation dictionary is not semantically consistent, as we do `root_document.class_words[abbreviation].class_word` for
access to class_word, but to iterate over abbreviations, we do `for abbreviation in root_document.class_words`. It has to
be `for abbreviation in root_document.class_word_abbreviations` - DONE
13. Update schema of `model` to accommodate class words list, to be accessible as root_document.class_words for a
simpler consumption during analysis. - DONE
14. Add `tests` to have integrated testing for `remodel`, `remap`, `analyze` modules. - DONE
15. Add `unit tests`, to include tests for `ncna.ini` file configuration parsing. - DONE
16. **Update `.gitignore`** to include files in `reports/*.xlsx`, as they are not compatible for version management.
More such kind of files are and longer they stay in a git repo, makes the git folder, that heavy to download and
maintain, as `full size blobs` are generated for every file recreation, while providing no easy way to check on the changes
to output while modifying the logic in package. Have to close and open the files again to see changes and `git diff`
doesn't work xlsx files. Thus have to limit version managed xlsx files to one it root directory of package, one in
distributed package directory, both are replica of other, and don't change often. Second one is a copy of first, not
programmatically assembled, thus would not generate blobs unnecessarily. - DONE
    1. Instead revisit `save_to_csv` function discarded earlier, to be used optionally during development, to track diff
 changes of output easily. - DONE
17. Serialize output reports - `ClassWordAnalysis` and other objects - TODO
18. Explore the option of adding support for `set` data type in `sob` package. This makes for an efficient lookup of
 set of list of strings in python, instead of looking up the list - ONGOING
    1. going with trying to get set supported by `sob` isn't the best option,as oapi also needs updates to support set,
    which isn't part of OpenAPI/JSON recognized data types, which `sob` primarily servers
    2. Explore hooks in sob to support set - TODO
19. Explore `marshmellow` package to do custom serialization, deserialization, to support `set` - TODO
20. Explore custom JSON Encoders , Decoders  to do custom serialization, deserialization, to support `set` - TODO
21. Revisit `extract_catalog` function, to be not called from `__main__`, rather used with in `AttributeNameAnalyzer`
object? - TODO
22. Explore, `write_to_xlsx` refactoring to be object-oriented. - TODO
23. Add `unit tests` to validate class word analysis logic, for different cases of outputs of the reports.
The tests should fail on the alteration of SAMPLE DATA or logic - TODO
24. Add `unit tests` for full_words_used, approved_abbreviations_used logic - TODO
25. Refactor the code base. - DONE
    1. Move `save_to_xlsx`, `save_to_csv` code from `utilities.py`, into the `analyze.py` module,
    to avoid circular dependency while applying type hinting.
    2. rename LONG_FORM_WORD, non_shortened_words to rename as FULL_WORDS_USED, full_words,
    as they are semantically accurate.
     The name non_shortened_words presumes, only the use of violated abbreviations in naming, but there also
    combinedwords that are being used. Thus, FULL_WORD captures the intention behind it, better.
    3. move `analyze_entity` and `analyze_entities` functions into `__main__.py`.
26. Add Exception handling where needed - TODO

#### Functionality
1. **Compare and analyse catalog data sets** provided by Confluence and Collibra. - DONE
2. **Create a CLI** based lookup with all the approved abbreviations, and generate reports of list of abbreviated words
missed, and list of long form words used in naming columns. - DONE
3. **Release two versions** - One for confluence based catalog, one for Collibra based catalog, for the
purposes of initial reporting. - DONE
4. Extend the functionality to **analyze entities in a given folder** with single command. - DONE
5. **Move away from using mandatory options** `--column-names-file`, `--column-names-folder` to pass file or
folder. This goes against the purpose of options, as the name suggests, they are "options", but current setup of
the tool, forces you to use one of them, for analysis.
6. Add `Class Word rules` in Confluence, to the analysis report(display warnings where they weren't used at the end) - DONE
7. Expand `USED_CATALOG.json` to also include column name for the respective entry. As same shortform can possibly be
used in different columns, with different meanings. This report is intended to avoid unapproved usage of abbreviations
for phrases or words it wasn't meant for - DONE
8. Change `reports` folder structure to have just one `catalog.json` file at the root of reports folder, as it is
common for all entities - DONE
9. Move away from using `analyze` command in CLI, as it is redundant. The CLI does just analysis at this point
and possibility of other commands like "create-suggested-names" sound either redundant or too far away, to justify
`analyze` command - DONE
10. Enable **analysis customization** for end users who need to add extra class words, acronyms - on a need basis through
`ncna.ini` file - Helps compile the list of words in need of enterprise approval to be added to the catalog. Makes report
 generation configurable - DONE
11. Update `analyze.py` module to accommodate the extra catalog - DONE
12. **Update logic of class word analysis** rules to differentiate for the correct class word abbreviation usage in
the middle of column name. - DONE
13. Add `ATTRIBUTE_NAMING_GUIDELINES_AND_REPORT_USAGE.html` to output - On the execution of CLI,
**generate an HTML page**, with brief description of reports generated and functionality of
the package. Use `marko` package as CI dependency for `html` generation, from the markdown file
maintained with the same name, and `html` file would be distributed as part of package - DONE
    1. Design it such that `marko` is a CI/TEST dependency, not package dependency,
    to keep the package dependencies fewer
    2. also for quick loading of HTML by just copying pre-generated one, rather than generating it.
14. Change format of output catalog from `catalog.json` to `CATALOG.xlsx` file, for easier consumption by end users to
look up list of approved abbreviations. Move dependency of `openpyxl` into package dependency - DONE
15. Update `CLASS_WORD_ANALYSIS` to consider the list of class words which warrant an additional postfix.
Ex: Wdth_M, Hght_CM, Wt_KG. - DONE
16. Output a single `ENTITY_NAME.xlsx` file in reports folder, instead of 3 files (`CLASS_WORD_ANALYSIS.csv`,
`LONG_FORM_WORD.csv`, `USED_CATALOG.json`) in a table specific folder - for a less cluttered reports folder and a
better end user experience. End users can now  have single file per object to deal with and readily filter on results
to focus on the columns they wanted easily. Also remove henceforth redundant code of saving to CSVs - DONE
17. **Format header rows** of sheets in `ENTITY_NAME_REPORT.xlsx` to be bold, for a better report reading experience - DONE
18. **Customize width of all columns** in 3 sheets, to make column width more appropriate for the respective data it holds.
So that end user, doesn't have to constantly adjust column width of all columns in all sheets, post every report
generation, to clearly see the analysis results. - DONE
19. Update `ATTRIBUTE_NAMING_GUIDELINES_AND_REPORT_USAGE.md` to add analysis on different solutions to propagate naming standards
across the enterprise - DONE
20. Update to `CLASS_WORD_ANALYSIS` schema to include additional notes column, to be used for extra feedback.
21. Add additional class words to `CATALOG.xlsx` - DONE
22. Update Logic of class words analysis to report `no` with the usage of full class word at the end. - DONE
23. To avoid unintended behavior in CLI, Use `argparse` library for parsing optional and `target-path` arguments. - DONE
24. Update `ATTRIBUTE_NAMING_GUIDELINES_AND_REPORT_USAGE.md` for better readability, also expand on the way forward for the tool. - DONE
25. End users provide input entities as multiple sheets in a single xlsx file, rather than a list of csv files.
For better end user experience and better control over data analyzed - from development standpoint -
currently, when given a folder, it analyzes data in all .csv files, even if they are not related. Analysts would
just want to give a xlsx file and expect more predictable execution - TODO
26. Allow for the option of analyzing a single sheet as provided, rather than generating reports for all sheets - TODO
27. Support variations in input column names text file(currently being read as comma separated values).
    1. support for multiple names in a row. - DONE
    2. support for leading and trailing spaces. - DONE
    3. support for spaces between names in a row without a comma separation. - DONE
28. Figure out a way to get `alias` information printed in the `help text` when running `column-name-analyzer -h`
w/o going for`_print_help()` method - TODO
29. Update `ATTRIBUTE_NAMING_GUIDELINES_AND_REPORT_USAGE.md` with a `FUTURE DEVELOPMENT` section. - DONE
30. Extend `LONG_FORM_WORD` sheet to have a new column, `MEANING`, whose value is generated for every
`LONG_FORM_WORD` by looking up a ENGLISH LANGUAGE words catalog of an `NLTK` library. The value in the column for
a given word, would give further feed back on, if that is what they mean. - TODO
    1. If the column is empty, then there is no english word with that name
    2. If there is value in column, ensure that column is used for one of the meanings mentioned, not a short form word
    with the same text.
33. Modifications to used catalog
    1. acronyms used at the end of the column are not appearing in catalog used - DONE
    2. remove abbreviations of class words in the used catalog - as it doesn't provide additional value, while adding
    a lot of additional info in the report. All the information needed is already included in CLASS WORD ANALYSIS report.
    3. Rename `APPROVED ABBREVIATIONS USED` sheet to `APPROVED ACRONYMS USED`, as it going forward would only include list of
    approved acronyms used.
34. Add `AGGREGATE` section to catalog, and incorporate related rules into analysis.

