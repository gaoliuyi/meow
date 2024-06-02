# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:13:03 2024

@author: ghp
"""

n,m=map(int,input().split())
w=list(map(int,input().split()))
g=[[] for i in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
ans=0
visited=[False]*n
def dfs(node):
    visited[node]=True
    a=w[node]
    for x in g[node]:
        if not visited[x]:
            a+=dfs(x)
    return a
for i in range(n):
    if not visited[i]:
        ans=max(ans,dfs(i))
print(ans)
    