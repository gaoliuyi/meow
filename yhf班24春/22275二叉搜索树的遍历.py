# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 10:55:01 2024

@author: ghp
"""

n=int(input())
ls=[0]*(n+1)
rs=[0]*(n+1)
num=list(map(int,input().split()))
i=1
x=num[0]
def insert(i,x):
    if num[i]<x:
        if ls[x]==0:
            ls[x]=num[i]
        else:
            insert(i,ls[x])
    if num[i]>x:
        if rs[x]==0:
            rs[x]=num[i]
        else:
            insert(i,rs[x])
for i in range(1,n):
    insert(i,x)
def printx(x):
    if x:
        printx(ls[x])
        printx(rs[x])
        print(x,end=' ')
    return
printx(x)
    
    
    