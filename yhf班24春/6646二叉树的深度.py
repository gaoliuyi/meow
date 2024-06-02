# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 09:06:20 2024

@author: ghp
"""

n=int(input())
depth=[1]*(n+1)
for i in range(1,n+1):
    a,b=map(int,input().split())
    if a!=-1:
        depth[a]=depth[i]+1
    if b!=-1:
        depth[b]=depth[i]+1
print(max(depth))