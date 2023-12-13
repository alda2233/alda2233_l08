"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-12-09"
-------------------------------------------------------
"""
# Imports
from asa import list_stats
# Constants
values = [94, 96, -22, -79, -28, -26, -50, 71, 24, -32]
smallest, largest, total, average = list_stats(values)
print(f"{smallest}, {largest},{total},{average}")
