"""
Creating a validator that checks if a string is a palindrome
"""
from collections import deque
def is_palindrome(value_enter):
    """ Function to check if palindrome"""
    if not isinstance(value_enter, str): #raise error if value_enter not string
        raise ValueError("Only string can be used in the function")

    length = len(value_enter)#count length of value_enter
    d_value = deque(value_enter)#converts value_enter to a deque and assigned to variable
    d_value.extendleft(value_enter)#adds value_enter to the left of the deque
    check_1 = list(d_value)#convetrs the deque to list and assigned to variable
    d_value.rotate(length) #in the deque the characters are rotated by the lenght
    check_2 = list(d_value)#converts the new deque to list

    check_bool = True
    if not value_enter:#checks if value_enter is blank and check_bool becomes false
        check_bool = False
    elif check_1 == check_2:#checks if check_1 and check_2 are equal
        check_bool = True
    else:#if check_1 and check_2 not equal then check_bool is false
        check_bool = False

    return check_bool
