# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:51:06 2024

@author: ghp
"""

from heapq import *
def dijk(n,g,start):
    dis=[float('inf')]*(n+1)
    dis[start]=0
    pq=[(0,start)]
    while pq:
        d,now=heappop(pq)
        if d>dis[now]:
            continue
        dis[now]=d
        for u,v in g[now]:
            newdis=dis[now]+v
            if newdis<dis[u]:
                dis[u]=newdis
                heappush(pq,(newdis,u))
    return dis
n,m=map(int,input().split())
g=[[] for i in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())    
    g[a].append((b,c))
start=1
ans=dijk(n,g,start)
print(ans[-1])