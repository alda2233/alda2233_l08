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
from functions import get_weekday_name
# Constants


while True:
    user_input = int(input("Enter a day number (1-7): "))
    if 1 <= user_input <= 7:
        day_name = get_weekday_name(user_input)
        print(f"{day_name}")
        break
