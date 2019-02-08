# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 21:07:34 2019

@author: Abdullah
"""
import math

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
    
    num = 4#int(input())
    print("Size: "+str(num)+" x "+str(num*3))
    print_doormat(num,num*3)   

    print(9//2)   
        
          
        
            
        
        

