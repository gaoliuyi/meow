# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 08:18:59 2024

@author: ghp
"""

di = [(-1, 0), (0, -1), (0, 1), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

ans=0
def dfs(x, y):
    global ans
    if g[x][y] == 'W':
        ans += 1
        g[x][y] = '.'
        for i in range(8):
            dx, dy = di[i]
            nx = x + dx
            ny = y + dy
            dfs(nx, ny)
    return



for i in range(int(input())):
    n, m = map(int, input().split())
    g = [['.'] * (m + 2)]
    for j in range(n):
        g.append(['.']+list(input())+['.'])
    g.append(['.'] * (m + 2))
    a = 0
    for x in range(1, n+1):
        for y in range(1, m+1):
            if g[x][y] == "W":
                ans = 0
                dfs(x, y)
                a = max(a, ans)
    print(a)

    