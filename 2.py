with open("input.txt", 'r') as f:
    strategy_guide = f.read().split('\n')[:-1]

total = 0
for game in strategy_guide:
    move, outcome = game.split(' ')
    move = ord(move) - ord('A')
    outcome = ord(outcome) - ord('X')
    response = (move + outcome - 1) % 3
    total += (3 * outcome) + response + 1
print(total)
