with open("input.txt", "r") as f:
    input = f.read()
crates, steps = input.split('\n\n')
stacks = []
for c in crates.split('\n')[:-1]:  
    for i in range(len(crates.split('\n')[0])):
        if (i - 1) % 4 == 0:
            if (i -1) // 4 >= len(stacks):
                stacks.append([])
            if c[i] != ' ':
                stacks[(i-1)//4].append(c[i])
for s in steps.split('\n')[:-1]:
    amount = int(s.split(' ')[1])
    src = int(s.split(' ')[3])-1
    dest = int(s.split(' ')[5])-1
    [stacks[dest].insert(0, v) for v in stacks[src][:amount][::-1]]
    stacks[src] = stacks[src][amount:]
[print(z[0][0]) for z in zip(stacks)]