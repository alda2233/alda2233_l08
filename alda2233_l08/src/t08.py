"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-11-10"
-------------------------------------------------------
"""
# Imports
from functions import linear_search
# Constants


values = input("Enter values separated by spaces: ").split()
values = [int(val) for val in values]

search_value = int(input("Enter the value to search: "))

result = linear_search(values, search_value)
print(result)
