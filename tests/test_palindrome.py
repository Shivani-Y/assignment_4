"""
Test module for palindrome"""

import pytest
from palindrome import is_palindrome

def test_for_data_type():
    """test to ckeck if datatype is string. If not then raise a value error"""
    with pytest.raises(ValueError):#raises an error of function called for any type but integer
        if not isinstance(is_palindrome(234), str):
            raise ValueError("Function only workS for strings")
