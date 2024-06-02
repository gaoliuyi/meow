# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:42:31 2024

@author: ghp
"""

from collections import defaultdict
from heapq import *


def toposort(g):
    ind = defaultdict(int)
    ans = []
    h = []
    for u in g:
        for y in g[u]:
            ind[y] += 1
    for u in range(1,v+1):
        if ind[u] == 0:
            heappush(h, u)
    while h:
        u = heappop(h)
        ans.append(u)
        if u in g:
            for y in g[u]:
                ind[y] -= 1
                if ind[y] == 0:
                    heappush(h, y)

    return ans


v, a = map(int, input().split())
g = {}
for _ in range(a):
    b, c = map(int, input().split())
    if b not in g:
        g[b] = [c]
    else:
        g[b].append(c)
ans = toposort(g)
if ans:
    for i, vertex in enumerate(ans):
        if i < len(ans) - 1:
            print(f"v{vertex}", end=" ")
        else:
            print(f"v{vertex}")
else:
    print("No topological order exists due to a cycle in the graph.")


    
        