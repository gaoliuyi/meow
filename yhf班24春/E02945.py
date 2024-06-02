# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:11:08 2024

@author: ghp
"""

k=int(input())
dp=[1]*k
p=list(map(int,input().split()))
for i in range(1,k):
    for j in range(i):
        if p[j]>=p[i]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))