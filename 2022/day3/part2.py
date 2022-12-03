import os

class Rucksack:
    def __init__(self, items):
        items = items.strip()
        self.allItems = items
        half_len = int(len(items)/2)
        self.firstCompartment = items[:half_len]
        self.secondCompartment = items[half_len:]

    def get_wrong_item(self):
        for i in self.firstCompartment:
            if i in self.secondCompartment:
                return(i)

    def get_priority(self, letter):
        if 97 <= ord(letter) <= 122:
            return(ord(letter)-97+1)
        else:
            return(ord(letter)-65+27)

def main():
    file = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')
    lines = file.readlines()


    total = 0
    for i in range(0, len(lines), 3):
        rucksacks = []
        rucksacks.append(Rucksack(lines[i]))
        rucksacks.append(Rucksack(lines[i+1]))
        rucksacks.append(Rucksack(lines[i+2]))

        badge = ""
        for letter in rucksacks[0].allItems:
            if not letter in rucksacks[1].allItems:
                continue
            if not letter in rucksacks[2].allItems:
                continue
            else:
                badge = letter
                break

        total = total + rucksacks[0].get_priority(badge)

    print(total)

if __name__=="__main__":
    main()