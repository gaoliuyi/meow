# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 10:34:50 2024

@author: ghp
"""
from heapq import heappop,heappush
def dijkstra(graph,start,end):
    dis={place:float("inf") for place in places}
    pq=[(0,start)]
    dis[start]=0
    path={place:None for place in places}
    while pq:
        distance,node=heappop(pq)
        if distance>dis[node]:
            continue
        if node==end:
            return path
        for place,cost in graph[node].items():
            newdistance=distance+cost
            if newdistance<dis[place]:
                dis[place]=newdistance
                path[place]=node
                heappush(pq,(newdistance,place))
n=int(input())
places=[input().strip() for i in range(n)]
graph={place:{} for place in places}
q=int(input())
for i in range(q):
    a,b,c=input().split()
    c=int(c)
    graph[a][b]=c
    graph[b][a]=c
r=int(input())
for _ in range(r):
    a,b=input().split()
    if a==b:
        print(a)
        continue
    path=dijkstra(graph,a,b)
    way=[b]
    x=b
    while path[x] is not None:
        way.append(path[x])
        x=path[x]
    ans=''
    for i in range(len(way)-1,0,-1):
        ans+=f"{way[i]}->({graph[way[i]][way[i-1]]})->"
    ans+=f"{b}"
    print(ans)
        
