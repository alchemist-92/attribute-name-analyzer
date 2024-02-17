import typing

import sob


class Acronyms(sob.model.Dictionary):
    """
    A mapping of ACRONYMS to a list of phrases which they are approved to be
    used for.
    """

    def __init__(
        self,
        items: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[str, "Phrases"],
            typing.Iterable[typing.Tuple[str, "Phrases"]],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
    ) -> None:
        super().__init__(items)


class Aggregate(sob.model.Object):
    """
    One or more phrases acronym to be used for

    Properties:

    - phrase
    - sample_usage
    - when_to_use
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[str, sob.abc.MarshallableTypes],
            typing.Iterable[typing.Tuple[str, sob.abc.MarshallableTypes]],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        phrase: typing.Optional[str] = None,
        sample_usage: typing.Optional[str] = None,
        when_to_use: typing.Optional[str] = None,
    ) -> None:
        self.phrase = phrase
        self.sample_usage = sample_usage
        self.when_to_use = when_to_use
        super().__init__(_data)


class Aggregates(sob.model.Dictionary):
    """
    A mapping of aggregate acronyms to its usage
    """

    def __init__(
        self,
        items: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[str, "Aggregate"],
            typing.Iterable[typing.Tuple[str, "Aggregate"]],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
    ) -> None:
        super().__init__(items)


class CatalogDocument(sob.model.Object):
    """
    The root document for the catalog

    Properties:

    - class_word_abbreviations:
      A dictionary mapping abbreviated class words to class words and usage
      information about each.
    - class_words:
      A collection of  class words.
    - acronyms:
      A mapping of ACRONYMS to a list of phrases which they are approved to be
      used for.
    - aggregates:
      A mapping of aggregate acronyms to its usage
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[str, sob.abc.MarshallableTypes],
            typing.Iterable[typing.Tuple[str, sob.abc.MarshallableTypes]],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        class_word_abbreviations: typing.Optional[
            "ClassWordAbbreviations"
        ] = None,
        class_words: typing.Optional["ClassWords"] = None,
        acronyms: typing.Optional["Acronyms"] = None,
        aggregates: typing.Optional["Aggregates"] = None,
    ) -> None:
        self.class_word_abbreviations = class_word_abbreviations
        self.class_words = class_words
        self.acronyms = acronyms
        self.aggregates = aggregates
        super().__init__(_data)


class ClassWordAbbreviation(sob.model.Object):
    """
    Information about a class word.

    Properties:

    - abbreviation
    - class_word
    - sample_usage
    - when_to_use
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[str, sob.abc.MarshallableTypes],
            typing.Iterable[typing.Tuple[str, sob.abc.MarshallableTypes]],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        abbreviation: typing.Optional[str] = None,
        class_word: typing.Optional[str] = None,
        sample_usage: typing.Optional[str] = None,
        when_to_use: typing.Optional[str] = None,
    ) -> None:
        self.abbreviation = abbreviation
        self.class_word = class_word
        self.sample_usage = sample_usage
        self.when_to_use = when_to_use
        super().__init__(_data)


class ClassWordAbbreviations(sob.model.Dictionary):
    """
    A dictionary mapping abbreviated class words to class words and usage
    information about each.
    """

    def __init__(
        self,
        items: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[str, "ClassWordAbbreviation"],
            typing.Iterable[typing.Tuple[str, "ClassWordAbbreviation"]],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
    ) -> None:
        super().__init__(items)


class ClassWordAnalysisReport(sob.model.Dictionary):
    """
    A mapping of ACRONYMS to a list of phrases which they are approved to be
    used for.
    """

    def __init__(
        self,
        items: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[str, "ColumnNameClassWordAnalysis"],
            typing.Iterable[typing.Tuple[str, "ColumnNameClassWordAnalysis"]],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
    ) -> None:
        super().__init__(items)


class ClassWords(sob.model.Dictionary):
    """
    A collection of  class words.
    """

    def __init__(
        self,
        items: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[str, sob.model.Dictionary],
            typing.Iterable[typing.Tuple[str, sob.model.Dictionary]],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
    ) -> None:
        super().__init__(items)


class ColumnNameClassWordAnalysis(sob.model.Array):
    """
    Class word analysis of an column name.
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable["ColumnNameClassWordAnalysisUnit"],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
    ) -> None:
        super().__init__(items)


class ColumnNameClassWordAnalysisUnit(sob.model.Object):
    """
    Class Word Analysis Instance

    Properties:

    - column_name
    - word
    - analysis
    - class_word_rules_followed
    - additional_notes
    - when_to_use
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[str, sob.abc.MarshallableTypes],
            typing.Iterable[typing.Tuple[str, sob.abc.MarshallableTypes]],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        column_name: typing.Optional[str] = None,
        word: typing.Optional[str] = None,
        analysis: typing.Optional[str] = None,
        class_word_rules_followed: typing.Optional[str] = None,
        additional_notes: typing.Optional[str] = None,
        when_to_use: typing.Optional[str] = None,
    ) -> None:
        self.column_name = column_name
        self.word = word
        self.analysis = analysis
        self.class_word_rules_followed = class_word_rules_followed
        self.additional_notes = additional_notes
        self.when_to_use = when_to_use
        super().__init__(_data)


class Phrases(sob.model.Array):
    """
    One or more phrases acronym to be used for
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[str],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
    ) -> None:
        super().__init__(items)


class UsedAbbreviation(sob.model.Object):
    """
    This object records data pertaining to all instances of the usage of an
    approved abbreviation, and the abbreviation's approved usages

    Properties:

    - column_names
    - allowed_usages
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[str, sob.abc.MarshallableTypes],
            typing.Iterable[typing.Tuple[str, sob.abc.MarshallableTypes]],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        column_names: typing.Optional["UsedAbbreviationColumnNames"] = None,
        allowed_usages: typing.Optional[
            "UsedAbbreviationAllowedUsages"
        ] = None,
    ) -> None:
        self.column_names = column_names
        self.allowed_usages = allowed_usages
        super().__init__(_data)


class UsedAbbreviationAllowedUsages(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[str],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
    ) -> None:
        super().__init__(items)


class UsedAbbreviationColumnNames(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[str],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
    ) -> None:
        super().__init__(items)


class UsedAbbreviations(sob.model.Dictionary):
    """
    This object records data pertaining to all instances of the usage of all
    approved abbreviations, and the abbreviation's approved usages. This is for
    ensuring they are used only for approved usages.
    """

    def __init__(
        self,
        items: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[str, "UsedAbbreviation"],
            typing.Iterable[typing.Tuple[str, "UsedAbbreviation"]],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
    ) -> None:
        super().__init__(items)


sob.meta.dictionary_writable(Acronyms).value_types = (  # type: ignore
    sob.types.MutableTypes([Phrases])
)
sob.meta.object_writable(Aggregate).properties = (  # type: ignore
    sob.meta.Properties(
        [
            ("phrase", sob.properties.String()),
            ("sample_usage", sob.properties.String()),
            ("when_to_use", sob.properties.String()),
        ]
    )
)
sob.meta.dictionary_writable(Aggregates).value_types = (  # type: ignore
    sob.types.MutableTypes([Aggregate])
)
sob.meta.object_writable(CatalogDocument).properties = (  # type: ignore
    sob.meta.Properties(
        [
            (
                "class_word_abbreviations",
                sob.properties.Property(
                    types=sob.types.MutableTypes([ClassWordAbbreviations])
                ),
            ),
            (
                "class_words",
                sob.properties.Property(
                    types=sob.types.MutableTypes([ClassWords])
                ),
            ),
            (
                "acronyms",
                sob.properties.Property(
                    types=sob.types.MutableTypes([Acronyms])
                ),
            ),
            (
                "aggregates",
                sob.properties.Property(
                    types=sob.types.MutableTypes([Aggregates])
                ),
            ),
        ]
    )
)
sob.meta.object_writable(ClassWordAbbreviation).properties = (  # type: ignore
    sob.meta.Properties(
        [
            ("abbreviation", sob.properties.String()),
            ("class_word", sob.properties.String()),
            ("sample_usage", sob.properties.String()),
            ("when_to_use", sob.properties.String()),
        ]
    )
)
sob.meta.dictionary_writable(  # type: ignore
    ClassWordAbbreviations
).value_types = sob.types.MutableTypes([ClassWordAbbreviation])
sob.meta.dictionary_writable(  # type: ignore
    ClassWordAnalysisReport
).value_types = sob.types.MutableTypes([ColumnNameClassWordAnalysis])
sob.meta.dictionary_writable(ClassWords).value_types = (  # type: ignore
    sob.types.MutableTypes([sob.model.Dictionary])
)
sob.meta.array_writable(  # type: ignore
    ColumnNameClassWordAnalysis
).item_types = sob.types.MutableTypes([ColumnNameClassWordAnalysisUnit])
sob.meta.object_writable(  # type: ignore
    ColumnNameClassWordAnalysisUnit
).properties = sob.meta.Properties(
    [
        ("column_name", sob.properties.String()),
        ("word", sob.properties.String()),
        (
            "analysis",
            sob.properties.Enumerated(
                types=sob.types.Types([str]),
                values={
                    "ABBREVIATED CLASS WORD IS USED AT THE END",
                    "ABBREVIATED CLASS WORD IS USED IN THE MIDDLE",
                    "AGGREGATE ACRONYM IS USED AT THE END",
                    "AGGREGATE ACRONYM IS USED IN THE MIDDLE",
                    "APPROVED ACRONYM IS USED AT THE END",
                    "CLASS WORD IS USED AS COLUMN NAME",
                    "FULL CLASS WORD IS USED AT THE END",
                    "FULL CLASS WORD IS USED IN THE MIDDLE",
                    "GENERIC WORD USED AT THE END",
                    "NO CLASS WORD IS USED IN THE NAME",
                    "UNIT SPECIFIC CLASS WORD MAY BE NEEDED AT THE END",
                },
            ),
        ),
        (
            "class_word_rules_followed",
            sob.properties.Enumerated(
                types=sob.types.Types([str]), values={"MAY BE", "NO", "YES"}
            ),
        ),
        ("additional_notes", sob.properties.String()),
        ("when_to_use", sob.properties.String()),
    ]
)
sob.meta.array_writable(Phrases).item_types = (  # type: ignore
    sob.types.MutableTypes([sob.properties.String()])
)
sob.meta.object_writable(UsedAbbreviation).properties = (  # type: ignore
    sob.meta.Properties(
        [
            (
                "column_names",
                sob.properties.Property(
                    types=sob.types.MutableTypes([UsedAbbreviationColumnNames])
                ),
            ),
            (
                "allowed_usages",
                sob.properties.Property(
                    types=sob.types.MutableTypes(
                        [UsedAbbreviationAllowedUsages]
                    )
                ),
            ),
        ]
    )
)
sob.meta.array_writable(  # type: ignore
    UsedAbbreviationAllowedUsages
).item_types = sob.types.MutableTypes([sob.properties.String()])
sob.meta.array_writable(  # type: ignore
    UsedAbbreviationColumnNames
).item_types = sob.types.MutableTypes([sob.properties.String()])
sob.meta.dictionary_writable(UsedAbbreviations).value_types = (  # type: ignore
    sob.types.MutableTypes([UsedAbbreviation])
)
# The following is used to retain class names when re-generating
# this model from an updated OpenAPI document
_POINTERS_CLASSES: typing.Dict[str, typing.Type[sob.abc.Model]] = {
    "#/components/schemas/acronyms": Acronyms,
    "#/components/schemas/aggregate": Aggregate,
    "#/components/schemas/aggregates": Aggregates,
    "#/components/schemas/catalog_document": CatalogDocument,
    "#/components/schemas/class_word_abbreviation": ClassWordAbbreviation,
    "#/components/schemas/class_word_abbreviations": ClassWordAbbreviations,
    "#/components/schemas/class_word_analysis_report": ClassWordAnalysisReport,
    "#/components/schemas/class_words": ClassWords,
    "#/components/schemas/column_name_class_word_analysis": ColumnNameClassWordAnalysis,
    "#/components/schemas/column_name_class_word_analysis_unit": ColumnNameClassWordAnalysisUnit,
    "#/components/schemas/phrases": Phrases,
    "#/components/schemas/used_abbreviation": UsedAbbreviation,
    "#/components/schemas/used_abbreviation/properties/allowed_usages": UsedAbbreviationAllowedUsages,
    "#/components/schemas/used_abbreviation/properties/column_names": UsedAbbreviationColumnNames,
    "#/components/schemas/used_abbreviations": UsedAbbreviations,
}
