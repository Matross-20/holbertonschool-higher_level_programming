#!/usr/bin/python3

def no_c(my_string):
    # Create a new string to hold the result
    new_string = ''

    # Iterate over each character in the original string
    for char in my_string:
        # Add the character to the new string if it is not 'c' or 'C'
        if char != 'c' and char != 'C':
            new_string += char

    # Return the new string
    return new_string
