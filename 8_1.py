with open("input.txt", "r") as f:
    rows = f.read().split('\n')[:-1]
count = 0
for r in range(len(rows)):
    for c in range(len(rows[r])):
        if c == 0 or c == len(rows[r])-1 or r == 0 or r == len(rows)-1 or rows[r][c] not in rows[r][c+1:] and rows[r][c] > max(rows[r][c+1:]) or rows[r][c] not in rows[r][0:c] and rows[r][c] > max(rows[r][0:c]) or rows[r][c] not in [row[c] for row in rows[:r]] and rows[r][c] > max([row[c] for row in rows[:r]]) or rows[r][c] not in [row[c] for row in rows[r+1:]] and rows[r][c] > max([row[c] for row in rows[r+1:]]):
            count += 1
print(count)

