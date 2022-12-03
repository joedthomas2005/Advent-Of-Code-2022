with open("input.txt") as f:
    rucksack_pairs = f.read().split('\n')[:-1]
sum = 0
for r in rucksack_pairs:
    shared = (set(r[:len(r)//2])&set(r[len(r)//2:])).pop()
    sum += ord(shared) - (38 if shared.isupper() else 96) # 38 is A - 27
print(sum)
