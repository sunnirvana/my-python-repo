"""[summary]
"""
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May',
                       'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# print(Month.__members__)

for name, member in Month.__members__.items():
    print(name, '=>', member, '=>', member.value)


@unique
class Weekday(Enum):
    Mon = 0
    Tue = 1
    Wed = 2
    Thu = 3
    Fir = 4
    Sat = 5
    Sun = 6


day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(day1 == Weekday.Mon)
print(day1 == Weekday.Tue)
print(Weekday(1))
print(day1 == Weekday(1))
for name, member in Weekday.__members__.items():
    print(name, '=>', member, '=>', member.value)

# Weekday(7)
