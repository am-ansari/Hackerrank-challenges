# -*- coding: utf-8 -*-

def print_diamond(size):
    alphArr = []
    for inc in range(num):
        alphArr.append(chr(97+inc))
    alphArr.reverse()
    
    # Code for top half of the diamond
    for j in range(size-1,-1,-1):
        idxL = [x for x in range(abs(size-j))]
        idxR = [x for x in range(abs(size-1-j))]
        idxR.reverse()
        # Printing top-left half
        print('-'*(size-len(idxL))*2,end="")
        for ele in idxL:
            print(alphArr[ele],end="")
            if ele != len(idxL)-1:
                print('-',end="")
        # Printing top-right half        
        for ele in idxR:
            print('-'+alphArr[ele],end="")     
        print('-'*(((size-len(idxR))*2)-2),end="")
        print("")    
    
    # Code for bottom half of the diamond  
    for j in range(size):
        idxL = [x for x in range(abs(size-j))]
        idxR = [x for x in range(abs(size-1-j))]
        idxR.reverse()
        if len(idxL)==size:
            continue
        # Printing bottom-left half
        print('-'*(size-len(idxL))*2,end="")
        for ele in idxL:
            print(alphArr[ele],end="")
            if ele != len(idxL)-1:
                print('-',end="")
        # Printing bottom-right half        
        for ele in idxR:
            print('-'+alphArr[ele],end="")     
        print('-'*(((size-len(idxR))*2)-2),end="")
        print("")  
        
if __name__ == '__main__':
    num = int(input("Enter size of the diamond greater than 1"))
    print_diamond(num)
            
        