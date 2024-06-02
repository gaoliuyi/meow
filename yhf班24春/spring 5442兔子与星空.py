# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 19:29:43 2024

@author: ghp
"""

from heapq import heapify,heappush,heappop
def prim(g,start):
    mst=[]
    used=set(start)
    path=[(cost,start,to) for to,cost in g[start].items()]
    heapify(path)
    while path:
        cost,start,to=heappop(path)
        if to not in used:
            used.add(to)
            mst.append(cost)
            for newto,newcost in g[to].items():
                if newto not in used:
                    heappush(path,(newcost,to,newto))
    return sum(mst)
n=int(input())
g={chr(i+65):{} for i in range(n)}
for i in range(n-1):
    edge=input().split()
    a=edge[0]
    nodes=int(edge[1])
    for j in range(nodes):
        star=edge[2*j+2]
        cost=int(edge[2*j+3])
        g[a][star]=cost
        g[star][a]=cost
print(prim(g,'A'))



