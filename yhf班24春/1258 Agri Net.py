# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:18:50 2024

@author: ghp
"""

from heapq import *
while True:
    try:
        n=int(input())
    except EOFError:
        break
    mat=[]
    d=0
    ans=0
    for i in range(n):
        mat.append(list(map(int,input().split())))
    v=set()
    h=[]
    heappush(h,(0,0))
    while h:
        x,y=heappop(h)
        if y in v:
            continue
        v.add(y)
        ans+=x
        dis=1e6
        for i in range(n):
            if mat[y][i]<dis:
                d=mat[y][i]
                heappush(h,(d,i))
    print(ans)
            
    