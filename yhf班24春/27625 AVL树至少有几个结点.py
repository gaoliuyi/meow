# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 16:44:45 2024

@author: ghp
"""
n=int(input())
dp=[0]*(n+1)
dp[1]=1
for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]+1
print(dp[n])