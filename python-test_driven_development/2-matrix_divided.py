#!/usr/bin/python3
""" 2-matrix_divided.py """


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int/float): The divisor.

    Returns:
        list of lists of float: A new matrix with all elements divided by div.

    Raises:
        TypeError: If the matrix contains non-numeric elements or rows of different sizes, 
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    # Check if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if all rows are of the same size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check for division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element by div and round to 2 decimal places
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    
    return new_matrix
