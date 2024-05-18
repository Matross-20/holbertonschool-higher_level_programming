#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Create a set to store unique integers
    unique_integers = set()

    # Iterate through the list and add each integer to the set
    for num in my_list:
        unique_integers.add(num)

    # Sum the unique integers
    return sum(unique_integers)
