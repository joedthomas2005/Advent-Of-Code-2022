with open("input.txt") as f:
    calories = f.read()
elves = calories[:-1].split('\n\n')
calories_per_elf = []
for elf in elves:
    elf_food = []
    foods = elf.split('\n')
    for food in foods:
        elf_food.append(int(food))
    calories_per_elf.append(sum(elf_food))
calories_per_elf.sort()
print(sum(calories_per_elf[-3:]))