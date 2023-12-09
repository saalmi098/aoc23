from typing import List, Dict

input_path: str = 'inputs/day08.txt'

with open(input_path, 'r') as file:
    lines: List[str] = [line.strip() for line in file.readlines()]

instructions: str = lines[0]
lines = lines[2:]

m: Dict[str, tuple[str, str]] = dict()
steps: int = 0
for line in lines:
    left: str = line.split(' ')[0]
    right: tuple[str, str] = tuple(line[line.index('(')+1:line.index(")")].split(', '))
    m[left] = right

# part 1
# curr_pos: str = "AAA"
# while curr_pos != "ZZZ":
#     curr_instr: str = instructions[steps % len(instructions)]
#     curr_pos = m[curr_pos][0] if curr_instr == "L" else m[curr_pos][1]
#     steps += 1

# part 2
def all_ghosts_finished(ghosts: List[str]) -> bool:
    for g in ghosts:
        if not g.endswith('Z'):
            return False
    return True

num_ghosts: int = sum(k.endswith('A') for k in m.keys())
ghost_positions: List[str] = list()

i: int = 0
for k, v in m.items():
    if not k.endswith('A'):
        continue

    ghost_positions.append(k)
    i += 1

while not all_ghosts_finished(ghost_positions):
    curr_instr: str = instructions[steps % len(instructions)]
    for i, ghost_pos in enumerate(ghost_positions):
        new_pos: str = m[ghost_pos][0] if curr_instr == "L" else m[ghost_pos][1]
        ghost_positions[i] = new_pos

    # TODO Optimization/better approach...
    
    steps += 1

print(steps)