# -*- coding: utf-8 -*-
"""
Printing a pattern as shown below (Size 7x21)
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------

"""
def print_doormat(n,m):

    midCol = n//2
    
    pattern = '.|.'
    ctr = 1
    for i in range(n):
        if i == midCol:
            print("WELCOME".center(m,'-'))
            ctr -= 2
        elif i < midCol:
            newpatter = pattern*ctr
            print(newpatter.center(m,'-'))
            ctr += 2
        else:
            newpatter = pattern*ctr
            print(newpatter.center(m,'-'))
            ctr -= 2
        
if __name__ == '__main__':
    
    num = int(input())
    print("Size: "+str(num)+" x "+str(num*3))
    print_doormat(num,num*3)   
 
        
          
        
            
        
        

