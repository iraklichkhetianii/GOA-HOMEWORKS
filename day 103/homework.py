#kata 1
import numpy
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    if(sq % numpy.sqrt(sq)==0):
        return numpy.square(numpy.sqrt(sq)+1)
    else:
        return -1
    

#kata 2

def solution(string, ending):
    return string.endswith(ending)