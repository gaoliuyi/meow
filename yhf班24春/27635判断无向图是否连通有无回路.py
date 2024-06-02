# -*- coding: utf-8 -*-
"""
Created on Mon May  6 10:42:22 2024

@author: ghp
"""

n,m=map(int,input().split())
g={i:[] for i in range(n)}
for _ in range(m):
    u,v=map(int,input().split())
    g[u].append(v)
    g[v].append(u)

def connect(g,n):
    i=1
    v=[False]*n
    stack=[0]
    v[0]=True
    while stack:
        node=stack.pop()
        for new in g[node]:
            if not v[new]:
                stack.append(new)
                v[new]=True
                i+=1
    if i==n:
        return True
def cycle(g,n):
    def dfs(node,v,father):
        v[node]=True
        for new in g[node]:
            if not v[new]:
                if dfs(new,v,node):
                    return True
            elif new!=father:
                return True
        return False
    v=[False]*n
    for i in range(n):
        if not v[i]:
            if dfs(i,v,-1):
                return True
    return False
if connect(g,n):
    print("connected:yes")
else:
    print('connected:no')
if cycle(g,n):
    print("loop:yes")
else:
    print('loop:no')