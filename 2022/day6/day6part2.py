import os
import operator as op



def is_valid_marker(marker:str):
    for c in marker:
        if op.countOf(marker, c) > 1:
            return False
    return True


def find_first_valid_marker(datastream:str):

    for i in range(0, len(datastream)):
        if is_valid_marker(datastream[i:i+14]):
            print(datastream[i:i+14])
            return(i+14)
    
    
def main():
    
    file = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')
    datastream = file.read()
    print(find_first_valid_marker(datastream))
   

if __name__=="__main__":
    main()