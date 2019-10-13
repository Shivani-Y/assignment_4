"""
Creating a validator that checks if a string is a palindrome
"""
def is_palindrome(value_enter):
    """ Function to check if palindrome"""
    if not isinstance(value_enter, str): #raise error if value_enter not string
        raise ValueError("Only string can be used in the function")

    check_bool = True
    if not value_enter:#checks if value_enter is blank
        check_bool = False

    return check_bool
