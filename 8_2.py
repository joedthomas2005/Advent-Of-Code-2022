with open("input.txt", "r") as f:
    rows = f.read().split('\n')[:-1]
best = 0
for r in range(len(rows)):
    for c in range(len(rows[r])):
        t_score = r
        l_score = c
        r_score = len(rows[r])-1-c
        b_score = len(rows)-1-r 
        for c_row in range(len(rows)):
            if int(rows[c_row][c]) >= int(rows[r][c]):
                if c_row < r:
                    t_score = r - c_row
                elif c_row > r and c_row - r < b_score:
                    b_score = c_row - r
        for c_col in range(len(rows[r])):
            if rows[r][c_col] >= rows[r][c]:
                if c_col < c:
                    l_score = c - c_col
                elif c_col > c and c_col - c < r_score:
                    r_score = c_col - c
        best = max(best, t_score * l_score * r_score * b_score)
print(best)
