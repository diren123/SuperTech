#!/usr/bin/python
from functools import total_ordering
from traceback import print_tb

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# 3a
length_of_belgium = len(Belgium)
print("-" * length_of_belgium)

# 3b
belgium_colon = Belgium.replace(',', ':')
print(belgium_colon)

#3c
fields = belgium_colon.split(':')

population_of_Belgium = int(fields[1])
population_of_Capital_City = int(fields[3])
total_population = population_of_Belgium + population_of_Capital_City

print(total_population)