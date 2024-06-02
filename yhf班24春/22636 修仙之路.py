# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 10:23:55 2024

@author: ghp
"""

ans=0
r,c=map(int,input().split())
dp=[[0]*c for i in range(r)]
d=[[-1,0],[0,-1],[1,0],[0,1]]
mat=[]
for i in range(r):
    mat.append(list(map(int,input().split())))
def dfs(x,y):
    if dp[x][y]>0:
        return dp[x][y]
    for i in range(4):
        dx=x+d[i][0]
        dy=y+d[i][1]
        if 0<=dx<r and 0<=dy<c and mat[x][y]>mat[dx][dy]:
            dp[x][y]=max(dp[x][y],dfs(dx,dy)+1)
    return dp[x][y]
for i in range(r):
    for j in range(c):
        ans=max(ans,dfs(i,j))
print(ans+1)