# -*- coding: utf-8 -*-

"""
Problem: Given an array containing only [0,1]; calculate the maximum number of
jumps to reach the end of array with the following conditions:
    1) Always skip 1
    2) Jump can be made in the increments of 1 or 2 only
Assumptions:
    1) Array always starts with 0
    2) Minimum size of array has to be 2 
    3) Array cannot contain continous 1 values
"""
def skipOnes(c):
    jump = 0
    newVal = 0
    while newVal < len(c)-1:
        if newVal+2 > len(c)-1:
            if newVal+1 > len(c)-1:
                break
            else:
                if c[newVal+1] == 0:
                    newVal +=1
                    jump+=1
                    break
                else:
                    break
                
        if c[newVal+2] == 0:
            newVal +=2
            jump+=1
        elif c[newVal+1] == 0:
            newVal +=1
            jump+=1
        else:
            continue
    return jump
            


if __name__ == '__main__':

    c = list(map(int, str(input()).split()))

    result = skipOnes(c)

    print(result)