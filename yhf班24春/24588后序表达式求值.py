# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 20:37:47 2024

@author: ghp
"""
n=int(input())
for i in range(n):
    a=input().split()
    stack=[]
    for x in a:
        if x in {"+","-","*","/"}:
            b=str(stack.pop())
            c=str(stack.pop())
            d=eval(c+x+b)
            stack.append(d)
        else:
            stack.append(float(x))
    print("{:.2f}".format(stack[0]))
        
        