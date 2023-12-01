import re
from enum import Enum

input_path = 'inputs/day01.txt'

class Number(Enum):
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9


with open(input_path, 'r') as file:
    lines = file.readlines()

sum = 0
for line in lines:
    line = line.strip().lower()

    # part 1
    # r = re.findall('[1-9]', line)
    # sum += int(r[0] + r[-1])

    # part 2
    r = re.findall('(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))', line)
    first = r[0] if r[0].isdigit() else str(Number[r[0]].value)
    last = r[-1] if r[-1].isdigit() else str(Number[r[-1]].value)
    sum += int(str(first) + str(last))
        
print(sum)