# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 17:35:04 2024

@author: ghp
"""

p=list(map(int,input().split()))
k=int(input())
n=len(p)
ans=0
for i in range(n):
    current=0
    for j in range(i,n):
        current+=p[j]
        if current==k:
            ans+=1
        
print(ans)
        