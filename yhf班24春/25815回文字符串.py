# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 10:29:00 2024

@author: ghp
"""

s=input()
n=len(s)
dp=[[0]*n for i in range(n)]
for l in range(2,n+1):
    for i in range(n-l+1):
        j=i+l-1
        if s[i]==s[j]:
            dp[i][j]=dp[i+1][j-1]
        else:
            dp[i][j]=min(dp[i+1][j-1],dp[i+1][j],dp[i][j-1])+1
print(dp[0][n-1])
            