from typing import List

input_path: str = 'inputs/day06.txt'

with open(input_path, 'r') as file:
    lines: List[str] = file.readlines()

duration: int = int(lines[0].replace(' ', '')[lines[0].index(':') + 1:])
distance: int = int(lines[1].replace(' ', '')[lines[1].index(':') + 1:])

res: int = 0
for t in range(duration + 1):
    dist = t*(duration-t)
    if (dist > distance):
        res += 1
    
print(res)