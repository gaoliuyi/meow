# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:16:28 2024

@author: ghp
"""
from collections import deque

dire=[(-1,0),(0,-1),(0,1),(1,0)]

n=int(input())
visited=[[0]*n for i in range(n)]
mat=[]
for i in range(n):
    mat.append(list(input()))
a=-1
b=-1
for i in range(n):
    for j in range(n):
        if mat[i][j]=='1':
            a=i
            b=j
            break
q=deque()
q.append((a,b))
visited[a][b]=1
nq=deque()  
def bfs():  
    while q:
        x,y=q.popleft()
        nq.append((x,y))
        for dx,dy in dire:
            nx=x+dx
            ny=y+dy
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny]==0 and mat[nx][ny]=='1':
                    q.append((nx,ny))
                    visited[nx][ny]=1
    step=0
    while nq:
        for _ in range(len(nq)):
            r,c=nq.popleft()
            for dx,dy in dire:
                nr=r+dx
                ny=c+dy
                if 0<=nr<n and 0<=ny<n and visited[nr][ny]==0:
                    visited[nr][ny]=1
                    if mat[nr][ny]=='1':
                        return step
                    nq.append((nr,ny))
        step+=1
    return step
print(bfs())
                    
        
        
        
            