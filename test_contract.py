from hypothesis import given, strategies as st
import pytest
from icontract import errors

from python_contract import sqrt_roundup

@given(x=st.floats(min_value=-10, max_value=10, allow_nan=False))
def test_sqrt_roundup_contracts(x):
    with pytest.raises(errors.ViolationError):
        sqrt_roundup(x)
