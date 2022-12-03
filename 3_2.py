with open("input.txt", 'r') as f:
    rucksacks = f.read().split('\n')[:-1]
sum = 0
for i in range(len(rucksacks)//3):
    shared = (set(rucksacks[i*3])&set(rucksacks[i*3+1])&set(rucksacks[i*3+2])).pop()
    sum += ord(shared) - (38 if shared.isupper() else 96)
print(sum)