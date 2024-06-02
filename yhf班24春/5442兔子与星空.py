# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 21:49:20 2024

@author: ghp
"""
from heapq import heapify,heappop,heappush
def prim(graph,start):
    mst=[]
    used=set()
    used.add(start)
    path=[(cost,start,to) for to,cost in graph[start].items()]
    heapify(path)
    while path:
        cost,start,to=heappop(path)
        if to not in used:
            used.add(to)
            mst.append([start,to,cost])
            for newto,newcost in graph[to].items():
                if newto not in used:
                    heappush(path,(newcost,to,newto))
    return mst
n=int(input())
graph={chr(i+65):{} for i in range(n)}
for i in range(n-1):
    edge=input().split()
    star=edge[0]
    nodes=int(edge[1])
    for j in range(nodes):
        tostar=edge[2+j*2]
        cost=int(edge[3+j*2])
        graph[star][tostar]=cost
        graph[tostar][star]=cost
mst=prim(graph,'A')
print(sum(x[2] for x in mst))
    
                  
            
        
    