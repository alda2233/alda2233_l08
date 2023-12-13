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
from functions import generate_integer_list
# Constants

n = int(input("Enter the number of values to generate: "))
low = int(input("Enter the low value range: "))
high = int(
    input("Enter the high value range (must be greater than the low value): "))

result = generate_integer_list(n, low, high)
print(result)
