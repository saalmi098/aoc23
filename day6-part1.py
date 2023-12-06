from typing import List

input_path: str = 'inputs/day06.txt'

with open(input_path, 'r') as file:
    lines: List[str] = file.readlines()

durations: List[int] = [int(x) for x in filter(None, lines[0].strip()[lines[0].index(':') + 1:].split(' '))]
distances: List[int] = [int(x) for x in filter(None, lines[1].strip()[lines[1].index(':') + 1:].split(' '))]

res: int = 1
for Ti, T in enumerate(durations):
    cnt: int = 0
    record = distances[Ti]
    for t in range(T + 1):
        dist = t*(T-t)
        if (dist > record):
            cnt += 1
    
    res *= cnt

print(res)