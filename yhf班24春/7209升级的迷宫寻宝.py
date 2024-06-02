# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 19:23:22 2024

@author: ghp
"""
import copy
dire=[(-1,0),(0,-1),(1,0),(0,1)]
from collections import deque
def bfs(start,end):
    q=deque()
    q.append([start])
    v=set()
    while q:
        ans=q.popleft()
        x=ans[-1][0]
        y=ans[-1][1]
        if [x,y]==end:
            return ans
        for dx,dy in dire:
            nx=x+dx;ny=y+dy
            if 1<=nx<=m and 1<=ny<=n and g[nx][ny]!='1' and (nx,ny) not in v:
                newans=copy.deepcopy(ans)
                newans.append([nx,ny])
                q.append(newans)
                v.add((nx,ny))
m,n=map(int,input().split())
g=[['1']*(n+1)]
for i in range(m):
    g.append([0]+list(input()))
for i in range(1,m+1):
    for j in range(1,n+1):
        if g[i][j]=='R':
            start=[i,j]
        if g[i][j]=='Y':
            mi=[i,j]
        if g[i][j]=="C":
            end=[i,j]
ans1=bfs(start,mi)
ans2=bfs(mi,end)
for i in range(len(ans1)-1):
    print(*ans1[i])
for i in range(len(ans2)):
    print(*ans2[i])
        
    