# -*- coding: utf-8 -*-
"""
Created on Mon May 27 10:37:31 2024

@author: ghp
"""

from heapq import *
n=int(input())
graph={chr(i+65):{} for i in range(n)}
for i in range(n-1):
    s=list(input())
    m=int(s[1])
    if m!=0:
        for j in range(2,2*m+1,2):
            graph[s[j]][s[0]]=int(s[j+1])
            graph[s[0]][s[j]]=int(s[j+1])
mst=[]
h=[]
heappush(h,(0,'A'))
v=set()
while h:
    x,y=heappop(h)
    if y in v:
        continue
    v.add(y)
    mst.append(y)
    for u in graph[v].keys():
        dis=graph[v][u]
        heappush(h,(dis,u))
print(sum(mst))
    