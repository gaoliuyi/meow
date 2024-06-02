# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 16:52:04 2024

@author: ghp
"""

n=int(input())
di=[(-2,-1),(-1,-2),(1,-2),(-2,1),(1,2),(2,1),(2,-1),(-1,2)]

vis=[[1]*n for i in range(n)]
def p(z):
    x,y=z
    edge=[]
    for i, j in di:
        nx = i + x
        ny = j + y
        if 0 <= nx < n and 0 <= ny < n and vis[nx][ny]==1:
            edge.append((nx,ny))
    return edge


def dfs(x,y,i):
    if i==n*n:
        return True
    vis[x][y]=10

    for nx,ny in sorted(p((x,y)),key=lambda z:len(p(z))):
        if vis[nx][ny]==1:
            if dfs(nx,ny,i+1):
                return True
            vis[nx][ny]=1
        else:
            break

sx,sy=map(int,input().split())
ans=dfs(sx,sy,1)
if ans:
    print('success')
else:
    print('fail')
    


            