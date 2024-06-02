# -*- coding: utf-8 -*-
"""
Created on Fri May 10 22:24:17 2024

@author: ghp
"""

l,m=map(int,input().split())
t=[1]*(l+1)
for i in range(m):
    a,b=map(int,input().split())
    for j in range(a,b+1):
        t[j]=0
print(sum(t))
        
