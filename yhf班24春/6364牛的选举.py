# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 23:18:05 2024

@author: ghp
"""

n,k=map(int,input().split())
cows=[]
for i in range(1,n+1):
    a,b=map(int,input().split())
    cows.append([i,a,b])
cows.sort(key=lambda x:-x[1])
cows=cows[:k]
cows.sort(key=lambda x:-x[2])
print(cows[0][0])
   