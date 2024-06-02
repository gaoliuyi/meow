# -*- coding: utf-8 -*-
"""
Created on Mon May 27 10:20:01 2024

@author: ghp
"""

from heapq import *
n,m=map(int,input().split())
graph={}
for i in range(m):
    u,v,c=map(int,input().split())
    if u in graph:
        graph[u][v]=c
    else:
        graph[u]={}
        graph[u][v]=c
    if v in graph:
        graph[v][u]=c
    else:
        graph[v]={}
        graph[v][u]=c
h=[]
ans=0
heappush(h,(0,1))
v=set()
while h:
    x,y=heappop(h)
    if y in v:
        continue
    v.add(y)
    ans=max(x,ans)
    for u in graph[y]:
        dis=graph[y][u]
        heappush(h,(dis,u))
print(n-1,ans)
        
        
    