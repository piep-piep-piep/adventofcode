from __future__ import annotations
import os

class Assignment:
    def __init__(self, start:int, end:int):
        self.start = start
        self.end = end
    def fully_containes(self, a:Assignment):
        return self.start <= a.start and self.end >= a.end
    def overlaps(self, a:Assignment):
        return self.start <= a.end and self.end >= a.start

def main():
    file = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')
    lines = file.readlines()

    count = 0
    for line in lines:
        line = line.strip()
        line = line.split(",")
        a1 = Assignment(int(line[0].split("-")[0]), int(line[0].split("-")[1]))
        a2 = Assignment(int(line[1].split("-")[0]), int(line[1].split("-")[1]))
        if a1.overlaps(a2):
            count += 1

    print(count)

if __name__=="__main__":
    main()