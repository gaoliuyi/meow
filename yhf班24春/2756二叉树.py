# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 09:15:40 2024

@author: ghp
"""

def up(x):
    if x==1:
        return 1
    elif x%2==0:
        return x//2
    else:
        return (x-1)//2
x,y=map(int,input().split())
while x!=y:
    if x>=2*y:
        x=up(x)
    elif y>=2*x:
        y=up(y)
    else:
        x=up(x)
        y=up(y)
print(x)