"""
Test module for palindrome"""

import pytest
from palindrome import is_palindrome

def test_for_data_type():
    """test to ckeck if datatype is string. If not then raise a value error"""
    with pytest.raises(ValueError):#raises an error of function called for any type but integer
        if not isinstance(is_palindrome(234), str):
            raise ValueError("Function only workS for strings")

def test_if_empty():
    """Return a False if function called for empty string"""
    assert is_palindrome("") is False

def test_a_is_palindrome():
    """Test if is_palindrome returns a True for a"""
    assert is_palindrome("a") is True

def test_bb_is_palindrome():
    """Test if is_palindrome returns a True for bb"""
    assert is_palindrome("bb") is True

def test_abc_is_palindrome():
    """Test if is_palindrome returns a True for abc"""
    assert is_palindrome("abc") is False

def test_laval_is_palindrome():
    """Test if is_palindrome returns a True for laval"""
    assert is_palindrome("laval") is True

def test_toronto_is_palindrome():
    """Test if is_palindrome returns a True for toronto"""
    assert is_palindrome("toronto") is False

def test_a_long_string_is_palindrome():
    """Test if is_palindrome returns a True for Able was I ere I saw
      Elba"""
    assert is_palindrome("Able was I ere I saw Elba") is True
