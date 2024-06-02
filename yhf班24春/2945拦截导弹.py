# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 09:53:37 2024

@author: ghp
"""

n=int(input())
k=list(map(int,input().split()))
dp=[0]*n
for i in range(1,n):
    for j in range(i):
        if k[i]<=k[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp)+1)