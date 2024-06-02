# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 10:03:38 2024

@author: ghp
"""
dp=[0]*31
dp[1]=1
dp[2]=1
for i in range(3,30):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
k=int(input())
print(dp[k])