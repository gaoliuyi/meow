# -*- coding: utf-8 -*-
"""
Created on Tue May 21 21:21:08 2024

@author: ghp
"""
from heapq import *
k=int(input())
n=int(input())
r=int(input())
road=[[] for i in range(n+1)]
for i in range(r):
    s,d,l,t=map(int,input().split())
    road[s].append((l,d,t))
def dijk(road):
    h=[]
    vis=set()
    heappush(h,(0,1,0))
    while h:
        l,s,t=heappop(h)
        
        if s==n:
            return l
        if (s,t) in vis:
            continue
        vis.add((s,t))
        if road[s]:
            for dis,ns,dt in road[s]:
                nl=l+dis
                nt=dt+t
                if nt<=k:
                    heappush(h,(nl,ns,nt))
                    
                   
                    
    return -1
print(dijk(road))

                
  