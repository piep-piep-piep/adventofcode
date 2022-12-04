import os

X = {
    "value" : 1,
    "A" : 3,
    "B" : 0,
    "C" : 6
}
Y = {
    "value" : 2,
    "A" : 6,
    "B" : 3,
    "C" : 0
}
Z = {
    "value" : 3,
    "A" : 0,
    "B" : 6,
    "C" : 3
}
D = {
    "X" : X,
    "Y" : Y,
    "Z" : Z
}


print(os.path.dirname(__file__))
file = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')
lines = file.readlines()

total = 0
for line in lines:
    line = line.strip().split(" ")
    result = D[line[1]][line[0]] + D[line[1]]["value"]
    total = total + result

print(total)