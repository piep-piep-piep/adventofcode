import os

class elf:
        
    def __init__(self, food_items):
        self.food_items = food_items

    def get_total_calories(self):
        total = 0
        for item in self.food_items:
            total = total + item
        return total


print(os.path.dirname(__file__))
file = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')
lines = file.readlines()

current_elf = elf([])
elves = []

for line in lines:
    if line.strip():    
        current_elf.food_items.append(int(line.strip()))
    else:
        elves.append(current_elf)
        current_elf = elf([])


max_calories = 0
for current_elf in elves:
    if current_elf.get_total_calories() > max_calories:
        max_calories = current_elf.get_total_calories()

print(max_calories)