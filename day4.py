from typing import List, Set, Dict

input_path: str = 'inputs/day04.txt'

with open(input_path, 'r') as file:
    lines: List[str] = file.readlines()

result: int = 0
cnt_cards: int = 0
copies: Dict[int, int] = dict()

for i, line in enumerate(lines):
    line = line.strip()[line.index(':')+2:]
    win_string, own_string = line.split(' | ')

    if not i in copies:
        copies[i] = 1

    for x in range(copies[i]):
        cnt_cards += 1
        winners: Set[int] = set()
        
        for val in list(filter(None, win_string.split(' '))):
            winners.add(int(val))

        # card_score: int = 0
        cnt_wins: int = 0
        for val in list(filter(None, own_string.split(' '))):
            if int(val) in winners:
                # part 1
                # card_score = 1 if card_score == 0 else card_score*2

                # part 2
                cnt_wins += 1

        # part 2
        for j in range(i + 1, cnt_wins + i + 1):
            if j in copies:
                copies[j] += 1
            else:
                copies[j] = 2

    # part 1
    # result += card_score

# print(result)
print(cnt_cards)