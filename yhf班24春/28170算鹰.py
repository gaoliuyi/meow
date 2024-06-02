# -*- coding: utf-8 -*-
"""
Created on Thu May  2 20:07:14 2024

@author: ghp
"""
ans=0
di=[(-1,0),(0,1),(0,-1),(1,0)]
def dfs(x,y):
    g[x][y]='-'
    for dx,dy in dir:
        nx=x+dx
        ny=y+dy
        if 0<=nx<n and 0<=ny<n:
            if g[nx][ny]===".":
                dfs(nx,ny)
n=int(input())
g=[]
for i in range(n):
    g.append(list(input()))
for i in range(n):
    for j in range(n):
        if g[i][j]==".":
            ans+=1
            dfs(i,j)
print(ans)
    