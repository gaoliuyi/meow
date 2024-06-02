# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:04:35 2024

@author: ghp
"""
from collections import deque
for _  in range(int(input())):
    n,m=map(int,input().split())
    graph={}
    for i in range(1,n+1):
        graph[i]=[]
    ind=[0]*(n+1)
    ind[0]=100
    for i in range(m):
        x,y=map(int,input().split())
        if x in graph:
            graph[x].append(y)
        ind[y]+=1
    def toposort(graph,n):
        ans=[]
        q=deque()
        for u in graph:
            if ind[u]==0:
                q.append(u)
        while q:
            a=q.popleft()
            ans.append(a)
            if graph[a]:
                for i in graph[a]:
                    ind[i]-=1
                    if ind[i]==0:
                        q.append(i)
                
           
        if len(ans)==n:
            return 'No'
        else:
            return 'Yes'
    print(toposort(graph,n))
        
        