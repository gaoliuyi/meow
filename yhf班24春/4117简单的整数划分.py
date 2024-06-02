# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 10:01:05 2024

@author: ghp
"""
while True:
    try:
        n=int(input())
        dp=[[0]*(n+1) for i in range(n+1)]
        for i in range(1,n+1):
            dp[i][0]=1
        dp[1]=[1]*(n+1)
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i<=j:
                    dp[i][j]=dp[i-1][j]+dp[i][j-i]
                else:
                    dp[i][j]=dp[j][j]
        print(dp[n][n])
    except EOFError:
        break