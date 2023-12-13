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
from functions import min_search
# Constants
values = input("Enter values separated by spaces: ").split()
values = [int(val) for val in values]

result = min_search(values)
print(result)
