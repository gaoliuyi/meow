# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 18:23:44 2024

@author: ghp
"""

s=input().split()
s.reverse()
stack=[]
for x in s:
    if x in {"+",'-','*','/'}:
        a=str(stack.pop())
        b=str(stack.pop())
        c=eval(a+x+b)
        stack.append(c)
    else:
        stack.append(float(x))
        
print("{:.6f}".format(stack[0]))
