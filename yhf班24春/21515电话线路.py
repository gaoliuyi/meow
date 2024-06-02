# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:54:46 2024

@author: ghp
"""
from heapq import *
inf=float('inf')
n,p,k=map(int,input().split())
dist=[[inf]*(k+1) for i in range(n+1)]
vis=[[False]*(n+1) for i in range(n+1)]
g={i:[] for i in range(n+1)}
for _ in range(p):
    a,b,l=map(int,input().split())
    g[a].append((b,l))
    g[b].append((a,l))
def dijkestra(r=1):
    dist[r][0]=0
    h=[(0,r,0)]
    while h:
        x,i,j=heappop(h)
        if vis[i][j]:
            continue
        vis[i][j]=True
        for v,w in g[i]:
            if dist[v][j]>max(x,w):
                dist[v][j]=max(x,w)
                heappush(h,(dist[v][j],v,j))
            if j<k and dist[v][j+1]>x:
                dist[v][j+1]=dist[i][j]
                heappush(h,(dist[v][j+1],v,j+1))
    return dist
dijkestra(1)
ans=inf
for i in range(k+1):
    ans=min(ans,dist[n][i])
if ans!=inf:
    print(ans)
else:
    print(-1)
    