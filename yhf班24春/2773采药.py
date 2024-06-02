# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 10:11:08 2024

@author: ghp
"""

t,m=map(int,input().split())
dp=[0]*(t+1)
for i in range(m):
    a,b=map(int,input().split())
    for j in range(t,a-1,-1):
        dp[j]=max(dp[j],dp[j-a]+b)
print(max(dp))