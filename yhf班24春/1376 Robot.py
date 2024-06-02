# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 19:39:11 2024

@author: ghp
"""

"""
Created on Sun Mar  3 18:58:35 2024

@author: ghp
"""

from collections import deque

x = [-1, 0, 1, 0]
y = [0, -1, 0, 1]


def bfs(bx, by, ex, ey, bd):
    quene = deque([(bx, by, 0, bd)])
    visited = [[[0] * 4 for i in range(m + 1)] for j in range(n + 1)]
    while quene:
        nx, ny, t, d = quene.popleft()
        if (nx, ny) == (ex, ey):
            return t
        for i in range(1, 4):
            ox = nx + x[d] * i
            oy = ny + y[d] * i
            if ox < 1 or ox >= n or oy < 1 or oy >= m or graph[ox][oy] or graph[ox - 1][oy] or graph[ox][oy - 1] or \
                    graph[ox - 1][oy - 1]:
                break
            if not visited[ox][oy][d]:
                if (ox, oy) == (ex, ey):
                    return t + 1
                visited[ox][oy][d] = 1
                quene.append((ox, oy, t + 1, d))
        nd = (d + 1) % 4
        if not visited[nx][ny][nd]:
            visited[nx][ny][nd] = 1
            quene.append((nx, ny, t + 1, nd))
        nd = (d - 1) % 4
        if not visited[nx][ny][nd]:
            visited[nx][ny][nd] = 1
            quene.append((nx, ny, t + 1, nd))
    return -1


while True:
    n,m = map(int, input().split())
    if (n, m) == (0, 0):
        break
    graph = [list(map(int, input().split()))+[0] for i in range(n)]
    bx, by, ex, ey, bd = input().split()
    bx = int(bx)
    by = int(by)
    ex = int(ex)
    ey = int(ey)
    if bd == 'north':
        bd = 0
    if bd == "west":
        bd = 1
    if bd == "south":
        bd = 2
    if bd == "east":
        bd = 3
    if (bx,by)==(ex,ey):
        print(0)
        continue
    print(bfs(bx, by, ex, ey, bd))
