# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 17:43:30 2024

@author: ghp
"""

di=[(-1,0),(0,-1),(1,0),(0,1)]
from heapq import heappop,heappush,heappify
def dijkestra(sx,sy,ex,ey):
    h=[]
    heappush(h,(0,sx,sy))
    visited=set()
    while h:
        t,x,y=heappop(h)
        if (x,y)==(ex,ey):
            return t
        visited.add((x,y))
        for dx,dy in di:
            nx=x+dx
            ny=y+dy
            if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited and g[nx][ny]!="#":
                nt=t+abs(int(g[nx][ny])-int(g[x][y]))
                heappush(h,(nt,nx,ny))
    return 'NO'
m,n,p=map(int,input().split())
g=[]
for i in range(m):
    g.append(input().split())
for _ in range(n):
    sx,sy,ex,ey=map(int,input().split())
    if g[sx][sy]=="#" or g[ex][ey]=="#":
        print("NO")
    else:
        print(bfs(sx,sy,ex,ey))
    

                
                
    