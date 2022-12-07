from __future__ import annotations
import os
from functools import reduce
import operator


class Terminal:


    def __init__(self, lines=[str]):
        self.lines = lines
        self.filesystem = {"/":{}}
        self.pwd = []
        self.lastcommand = None
        self.total_small_dicts_size = 0

    def parse_terminal(self, lines: list[str]):

        for i, line in enumerate(lines):
            if line.startswith("$ cd"):
                self.__parse_cd(line)
            elif line.startswith("$ ls"):
                self.lastcommand = "ls"
            else:
                if not self.lastcommand == "ls":
                    raise Exception("parsing directory even tho last command wasnt ls")
                self.__parse_ls_output_line(line)

    def get_dirs_sizes_with_limit(self, dir:dict, limit):
        dir_size = self.get_dir_size(dir)
        
        if dir_size <= 100000:
            self.total_small_dicts_size = self.total_small_dicts_size + dir_size
        for key, value in dir.items():
            if type(value) == dict:
                 self.get_dirs_sizes_with_limit(value, limit)

    def get_dir_size(self, dir:dict):
        total_size = 0
        for key, value in dir.items():
            if type(value) == str:
                total_size = total_size + int(value)
            else:
                total_size = total_size + self.get_dir_size(value)
        return total_size

    def __parse_cd(self, cmd:str):
        arg = cmd.split(" ")[-1]
        if(arg=="/"):
            self.pwd = ["/"]
        elif(arg==".."):
            self.pwd.pop()
        else:
            self.pwd.append(arg)
        self.lastcommand="cd"

    def __parse_ls_output_line(self, cmd:str):
        args = cmd.split(" ")
        if(args[0]=="dir"):
            folder_path = self.pwd.copy()
            folder_path.append(args[1])
            setInDict(self.filesystem, folder_path, {})
        else:
            file_path = self.pwd.copy()
            file_path.append(args[1])
            setInDict(self.filesystem, file_path, args[0])



def getFromDict(dataDict, mapList):
    return reduce(operator.getitem, mapList, dataDict)

def setInDict(dataDict, mapList, value):
    getFromDict(dataDict, mapList[:-1])[mapList[-1]] = value

    
def main():
    
    file = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    t = Terminal()
    t.parse_terminal(lines)
    print(t.filesystem)
    print(t.get_dirs_sizes_with_limit(t.filesystem, 10000))
    print(t.total_small_dicts_size)


if __name__=="__main__":
    main()