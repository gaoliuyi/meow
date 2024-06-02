# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 16:34:23 2024

@author: ghp
"""

m,n=map(int,input().split())
dp=[[0]*(m+1) for i in range(n+1)]
for i in range(1,n+1):
    dp[i][0]=1

dp[1]=[1]*(m+1)
for i in range(1,n+1):
    dp[i][1]=1
for i in range(1,n+1):
    for j in range(1,m+1):
        if i>j:
            dp[i][j]=dp[j][j]
        else:
            dp[i][j]=dp[i-1][j]+dp[i][j-i]
print(dp[n][m])
        
