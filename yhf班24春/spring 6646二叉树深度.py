# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 21:51:58 2024

@author: ghp
"""

n=int(input())
dp=[1]*(n+1)
for i in range(1,n+1):
    a,b=map(int,input().split())
    if a!=-1:
        dp[a]=dp[i]+1
    if b!=-1:
        dp[b]=dp[i]+1
print(max(dp))