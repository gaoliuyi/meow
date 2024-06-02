# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 17:53:08 2024

@author: ghp
"""


ans = 0
graph = [list(map(int, input().split(','))) for i in range(10)]


def dfs(r, c):
    if graph[r][c] == 1:
        return True
    if r == 0 or c == 0 or r == 9 or c == 9:
        return False

    graph[r][c] = 1
    up = dfs(r - 1, c)
    down = dfs(r + 1, c)
    left = dfs(r, c - 1)
    right = dfs(r, c + 1)

    return up and down and left and right


for i in range(1, 9):
    for j in range(1, 9):
        if graph[i][j] == 0 and dfs(i, j):
            ans += 1
print(ans)