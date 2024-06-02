# -*- coding: utf-8 -*-
"""
Created on Thu May  2 21:58:37 2024

@author: ghp
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May  2 21:58:37 2024

@author: ghp
"""

from heapq import *


def dijkestra(g, start, end):
    dis = {p: float('inf') for p in ps}
    path = {p: None for p in ps}
    dis[start] = 0
    h = [(0, start)]
    while h:
        cost, s = heappop(h)
        if cost > dis[s]:
            continue
        elif s == end:
            return path
        else:
            for ns, nc in g[s].items():
                nds = cost + nc
                if nds <= dis[ns]:
                    dis[ns] = nds
                    path[ns] = s
                    heappush(h, (nds, ns))


n = int(input())
ps = [input().strip() for i in range(n)]
g = {p: {} for p in ps}
q = int(input())
for _ in range(q):
    a, b, c = input().split()
    c = int(c)
    g[a][b] = c
    g[b][a] = c
r = int(input())
for i in range(r):
    s, e = input().split()
    if s == e:
        print(s)
    else:
        path = dijkestra(g, s, e)
        way = [e]
        x = e
        while path[x] is not None:
            way.append(path[x])
            x = path[x]
        ans = ''
        for i in range(len(way) - 1, 0, -1):
            ans += f"{way[i]}->({g[way[i]][way[i - 1]]})->"
        ans += f'{e}'
        print(ans)



    

    