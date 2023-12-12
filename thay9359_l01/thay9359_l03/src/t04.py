"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Navina Thayaruban
ID:      169069359
Email:   thaya9359@mylaurier.ca
__updated__ = "2023-09-25"
-------------------------------------------------------
"""

number = float(input("Enter number: "))
percent = float(input("Enter percent: "))

percentage = percent/ 100
percentage1 = percentage * number

print(f"A {percent} percent discount on {number} is {percentage1:.1f}")