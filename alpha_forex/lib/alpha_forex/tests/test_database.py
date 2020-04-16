# -------------------------------------------------------------------------------------------------
# Test Database Module
# -------------------------------------------------------------------------------------------------

import pytest
from .. import database


@pytest.mark.parametrize(
    ("value", "expected"),
    (
        ("1. From_Currency Code", "FROM_CURRENCY_CODE"),
        ("2. From_Currency Name", "FROM_CURRENCY_NAME"),
    )
)
def test_standardise(value, expected):
    assert database.standardise(value) == expected


@pytest.mark.parametrize(
    ("value", "expected"),
    (
        ("1", '1'),
        ("Test", '"Test"'),
        ("1.234", '1.234'),
    )
)
def test_enquote(value, expected):
    assert database.enquote(value) == expected
