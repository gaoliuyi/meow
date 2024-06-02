# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 19:21:34 2024

@author: ghp
"""

t=int(input())
for _ in range(t):
    num=list(map(int,input().split()))
    n=num[0]
    dp=[[0]*7 for x in range(n+1)]
    dp[0][0]=1
    for i in range(1,n+1):
        for j in range(7):
            dp[i][j]=dp[i-1][j]+dp[i-1][(j-num[i])%7]
    print(dp[n][0])