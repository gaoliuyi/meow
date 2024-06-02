# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 17:01:46 2024

@author: ghp
"""

from collections import deque

dire = [(-1, 0), (0, -1), (1, 0), (0, 1)]
flag = 0
ans = 0


def bfs(x, y, t):
    visited = set()
    global ans, flag
    q = deque()
    q.append((t, x, y, 0))
    while q:
        t, x, y, ans = q.popleft()
        for dx, dy in dire:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if g[nx][ny] != "#":
                    nt = t
                else:
                    nt = t - 1
                if nt >= 0 and (nt, nx, ny) not in visited:

                    newans = ans + 1
                    if g[nx][ny]=="+":
                        flag = 1
                        return flag,newans
                    q.append((nt, nx, ny, newans))
                    visited.add((nt, nx, ny))
    return flag,ans


m, n, t = map(int, input().split())
g = []
for i in range(m):
    g.append(list(input()))
for i in range(m):
    for j in range(n):
        if g[i][j] == "@":
            x = i
            y = j
flag,newans=bfs(x, y, t)
if flag:
    print(newans)
else:
    print(-1)









                
                    
                
                
    