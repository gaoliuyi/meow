# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 09:24:21 2024

@author: ghp
"""
di=[(-1,2),(-1,-2),(1,2),(1,-2),(2,1),(2,-1),(-2,-1),(-2,1)]
ans=0
def dfs(x,y,i):
    v[x][y]=1
    global ans
    if i==m*n-1:
        ans+=1
        return
    for dx,dy in di:
        nx=x+dx
        ny=y+dy
        if 0<=nx<n and 0<=ny<m and v[nx][ny]==0:
            dfs(nx,ny,i+1)
            v[nx][ny]=0
    return
for _ in range(int(input())):
    ans=0
    n,m,x,y=map(int,input().split())
    v=[[0]*m for i in range(n)]
    dfs(x,y,0)
    print(ans)
    
    