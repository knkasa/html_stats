from enum import Enum

# Define an Enum for days of the week
class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

# Accessing Enum members
print(Day.MONDAY)        # Output: Day.MONDAY
print(Day.MONDAY.name)   # Output: MONDAY
print(Day.MONDAY.value)  # Output: 1