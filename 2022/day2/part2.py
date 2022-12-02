import os

X = {
    "value" : 0,
    "A" : 3,
    "B" : 1,
    "C" : 2
}
Y = {
    "value" : 3,
    "A" : 1,
    "B" : 2,
    "C" : 3
}
Z = {
    "value" : 6,
    "A" : 2,
    "B" : 3,
    "C" : 1
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