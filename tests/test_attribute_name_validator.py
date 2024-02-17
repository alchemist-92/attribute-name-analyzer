# import os
import sys
import unittest
import importlib.util
from pathlib import Path
from types import ModuleType
from typing import Optional, Any
from importlib.machinery import ModuleSpec
from attribute_name_validator.analyze import (
    AttributeNameValidator,
    get_extra_catalog,
)
from attribute_name_validator.utilities import iter_csv_files

TEST_DIRECTORY_PATH: Path = Path(__file__).absolute().parent
TEST_ENTITIES_PATH: Path = TEST_DIRECTORY_PATH.joinpath("entities")
SCRIPTS_DIRECTORY_PATH: Path = TEST_DIRECTORY_PATH.parent.joinpath("scripts")


def import_script(script_name: str) -> Any:
    spec: Optional[ModuleSpec] = importlib.util.spec_from_file_location(
        script_name, SCRIPTS_DIRECTORY_PATH.joinpath(f"{script_name}.py")
    )
    assert isinstance(spec, ModuleSpec)
    module: ModuleType = importlib.util.module_from_spec(spec)
    sys.modules[script_name] = module
    assert spec.loader
    spec.loader.exec_module(module)
    return module


class TestAttributeNameValidator(unittest.TestCase):
    def test_attribute_name_validator(self) -> None:
        # remodel_objects: Any = import_script("remodel")
        # remodel_objects.main()
        # # To avoid tox failure, we need to restructure the autogenerated
        # # model.py module so that, black --check . won't fail, detecting
        # # formatting it can further do on the module
        # os.system("black .")
        update_catalog: Any = import_script("update_catalog")
        update_catalog.main()
        catalog: Any = get_extra_catalog()

        assert "LOB" in catalog.additional_acronyms
        assert "LB" in catalog.additional_class_word_abbreviations

        for column_names_file_path in iter_csv_files(TEST_ENTITIES_PATH):
            attribute_name_validator = AttributeNameValidator(
                column_names_file_path=column_names_file_path,
                extra_class_word_abbreviations=(
                    catalog.additional_class_word_abbreviations
                ),
                extra_acronyms=catalog.additional_acronyms,
                write_to_text_files=False,
            )
            attribute_name_validator.analyze_entity()
            attribute_name_validator.save_reports()

    def naming_rules_unit_tests(self) -> None:
        """
        TODO
        """
        pass


if __name__ == "__main__":
    unittest.main()
