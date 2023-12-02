import re
from functools import reduce

input_path = 'inputs/day02.txt'

with open(input_path, 'r') as file:
    lines = file.readlines()

max = { 'red': 12, 'green': 13, 'blue': 14 }

result = 0
curr_id = 1
for line in lines:
    line = line.strip().lower()
    line = line[line.index(':')+2:]
    
    tuples = re.split(', |; ', line)

    # part 1
    # fits = True
    # for tpl in tuples:
    #     (count, color) = tpl.split(' ')
    #     if (int(count) > max[color]):
    #         fits = False
    #         break
    # 
    # if (fits):
    #     result += curr_id
    #
    # curr_id += 1

    # part 2
    current_max = { 'red': 0, 'green': 0, 'blue': 0 }
    for tpl in tuples:
        (count, color) = tpl.split(' ')
        if (int(count) > current_max[color]):
            current_max[color] = int(count)
    
    power = reduce(lambda x, y: x*y, current_max.values())
    result += power
    
print(result)