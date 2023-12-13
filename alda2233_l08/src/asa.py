"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-12-11"
-------------------------------------------------------
"""
# Imports


def list_stats(values):
    """
    -------------------------------------------------------
    Returns statistics about values in a list.
    values has at least one element.
    Use: smallest, largest, total, average = list_stats(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of float)
    Returns:
        smallest - the smallest number in values (float)
        largest - the largest number in values (float)
        total - total of numbers in list (float)
        average - the average numbers in values (float)
    -------------------------------------------------------
    """

    values.sort()
    smallest = values[0]

    n = len(values)
    largest = values[n-1]

    i = 0
    total = 0
    for i in range(n):
        total += values[i]
    average = total/n

    return float(smallest), float(largest), float(total), float(average)
