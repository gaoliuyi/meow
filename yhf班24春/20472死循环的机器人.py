# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 08:47:13 2024

@author: ghp
"""

di=[(0,1),(-1,0),(0,-1),(1,0)]
x,y=0,0
i=0
s=input()
s=s*4
for k in s:
    if k=='G':
        dx=di[i][0]
        dy=di[i][1]
        x+=dx
        y+=dy
    elif k=='L':
        i=(i+1)%4
    elif k=='R':
        i=(i+3)%4
if (x,y)==(0,0):
    print(1)
else:
    print(0)