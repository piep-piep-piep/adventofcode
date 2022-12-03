import os

class Rucksack:
    def __init__(self, items):
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
    for line in lines:
        r = Rucksack(line.strip())
        total = total + r.get_priority(r.get_wrong_item())

    print(total)

if __name__=="__main__":
    main()