# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 21:12:39 2024

@author: ghp
"""

a=input().split()
stack=[]
for i in reversed(a):
    if i in {"+","-","*","/"}:
        b=str(stack.pop())
        c=str(stack.pop())
        d=eval(b+i+c)
        stack.append(d)
    else:
        stack.append(float(i))
print("{:.6f}".format(stack[0]))