with open("input.txt") as f:
    pairs = f.read().split('\n')[:-1]
num_duplicates = 0
for pair in pairs:
    elf1, elf2 = [[int(v) for v in p.split('-')] for p in pair.split(',')]
    elf1, elf2 = range(elf1[0], elf1[1]+1), range(elf2[0], elf2[1]+1)
    num_duplicates += int(set(elf1)<=set(elf2) or set(elf1)>=set(elf2))
print(num_duplicates)