"""
Creating a validator that checks if a string is a palindrome
"""
def is_palindrome(value_enter):
    """ Function to check if palindrome"""
    if not isinstance(value_enter, str):
        raise ValueError("Only string can be used in the function")
