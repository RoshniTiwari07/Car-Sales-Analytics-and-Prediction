import importlib.util
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
VALIDATION_PATH = PROJECT_ROOT / "scripts" / "mysql_validation.py"

spec = importlib.util.spec_from_file_location(
    "mysql_validation",
    VALIDATION_PATH,
)
if spec is None or spec.loader is None:
    raise ImportError(f"Cannot load validation module: {VALIDATION_PATH}")

validation_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validation_module)

validate_row_counts = validation_module.validate_row_counts


def test_matching_row_counts_pass():
    validate_row_counts(expected_rows=117, actual_rows=117)


def test_mismatched_row_counts_raise_value_error():
    with pytest.raises(
        ValueError,
        match="MySQL row count mismatch: expected 117, found 116",
    ):
        validate_row_counts(expected_rows=117, actual_rows=116)


def test_zero_row_counts_pass():
    validate_row_counts(expected_rows=0, actual_rows=0)
