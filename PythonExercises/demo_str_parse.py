#! /usr/bin/env python3
# Author: Diren Gunasekera
# Description: This script will demo string parsing with conditions

"""
    Docstring:
"""

try:
    with open("words", "r") as file:
        for count, line in enumerate(file, start=1):
            current_string = line.strip()

            if current_string.startswith("y") or current_string.endswith("n") or "town" in current_string:
                print(f"{count}: {current_string.upper()}")

except FileNotFoundError:
    print("Please Ensure The 'Words' File Exists In The Current Working Directory")
