from typing import List, Set

input_path: str = 'inputs/day03.txt'

def is_valid_pos(r: int, c: int) -> bool:
    return r >= 0 and r <= rows and c >= 0 and c <= cols

def get_adjacents_score(symbol_row: int, symbol_col: int, char: str) -> int:
    sum: int = 0
    adjacents: Set[str] = set()

    for r in range(symbol_row - 1, symbol_row + 2):
        if not is_valid_pos(r, 1):
            continue

        for c in range(symbol_col - 1, symbol_col + 2):
            if (not is_valid_pos(r, c) or (r == symbol_row and c == symbol_col)):
                continue

            if lines[r][c].isdigit():
                number_str: str = lines[r][c]
                tmp_c_left: int = c - 1
                while (is_valid_pos(r, tmp_c_left) and lines[r][tmp_c_left].isdigit()):
                    number_str = lines[r][tmp_c_left] + number_str
                    tmp_c_left -= 1

                tmp_c_right: int = c + 1
                while (is_valid_pos(r, tmp_c_right) and lines[r][tmp_c_right].isdigit()):
                    number_str += lines[r][tmp_c_right]
                    tmp_c_right += 1
            
                if not number_str in adjacents:
                    adjacents.add(number_str)
                    sum += int(number_str)

    # part 1
    # return sum

    # part 2
    if (len(adjacents) == 2):
        product = 1
        for val in adjacents:
            product *= int(val)
        return product
    return 0

with open(input_path, 'r') as file:
    lines: List[str] = file.readlines()

result: int = 0
rows = len(lines)
cols = len(lines[0])

for r, line in enumerate(lines):
    line = line.strip()

    for c, char in enumerate(line):
        if char != '.' and not char.isdigit():
            adjacents = {}
            result += get_adjacents_score(r, c, char)
    
print(result)