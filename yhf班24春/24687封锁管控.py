# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 21:00:10 2024

@author: ghp
"""

n,m=map(int,input().split())
a=list(map(int,input().split()))
p=[0]*(n+1)
for i in range(1,n+1):
    p[i]=p[i-1]+a[i-1]
dp=[[float('inf')]*(m+1) for i in range(n+1)]
for i in range(1,n+1):
    dp[i][0]=p[i]*i
for i in range(1,n+1):
    for j in range(1,min(i,m)+1):
        for k in range(j-1,i):
            dp[i][j]=min(dp[i][j],dp[k][j-1]+(i-k)*(p[i]-p[k]))
print(dp[n][m])
        