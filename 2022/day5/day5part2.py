import os
from collections import deque
import re


def main():
    ship = parse_ship('input_1.txt')
    moves = parse_moves('input_2.txt')
    ship = move_containers_preserve_order(ship, moves)
    top_containers = get_top_containers(ship)
    print("".join(top_containers))


def parse_ship(ship_input):
    file = open(os.path.join(os.path.dirname(__file__), ship_input), 'r')
    lines = file.readlines()

    number_of_stacks = len(lines[-1].strip().split("   "))
    matrix = [deque() for i in range(number_of_stacks)]
    for line in reversed(lines):
        if line.startswith(" 1 "):
            continue
        horizontal_container_list = [(line[i:i+4].strip("\n []")) for i in range(0, len(line), 4)]
        for index, container in enumerate(horizontal_container_list):
            if container != '':
                matrix[index].append(container)
    return matrix


def parse_moves(moves_input):
    file = open(os.path.join(os.path.dirname(__file__), moves_input), 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    moves = [list() for i in range(len(lines))]
    for index, line in enumerate(lines):
        pattern = r"move (\d+) from (\d+) to (\d+)"
        line_list = []
        for index2, value in enumerate(re.match(pattern, line).groups()):
            if index2 == 0:
                line_list.append(int(value))
            else:
                line_list.append(int(value)-1)
        moves[index] = line_list
    return(moves)


def move_containers(ship, moves):
    for move in moves:
        for i in range(move[0]):
            if len(ship[move[1]]) == 0:
                break
            ship[move[2]].append(ship[move[1]].pop())
    return ship


def move_containers_preserve_order(ship, moves):
    for move in moves:
        temp_stack = deque()
        for i in range(move[0]):
            if len(ship[move[1]]) != 0:
                temp_stack.append(ship[move[1]].pop())
        for i in range(len(temp_stack)):
            ship[move[2]].append(temp_stack.pop())
    return(ship)


def get_top_containers(ship):
    top_containers = []
    for stack in ship:
        top_containers.append(stack[-1])
    return(top_containers)


if __name__=="__main__":
    main()