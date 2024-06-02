# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 22:33:38 2024

@author: ghp
"""

w,n=map(int,input().split())
p=list(map(int,input().split()))
minh=n+1
left=0
current=0
for i in range(0,n):
    current+=p[i]
    while current>=w:
        minh=min(minh,i-left+1)
        
        current-=p[left]
        left+=1
if minh<=n:
    print(minh)
else:
    print(0)
    