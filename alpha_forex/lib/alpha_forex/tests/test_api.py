# -------------------------------------------------------------------------------------------------
# Test Module API
# -------------------------------------------------------------------------------------------------

import pytest
from .. import api


@pytest.mark.parametrize(
    ("d", "expected"),
    (
        ({"My Ugly Key": 1, "1. My Other key": 2}, {"MY_UGLY_KEY": 1, "MY_OTHER_KEY": 2}),
    )
)
def test_standardize_keys(d, expected):
    assert api.standardize_keys(d) == expected
