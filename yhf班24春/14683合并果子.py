# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:34:10 2024

@author: ghp
"""
from heapq import heappop,heappush,heapify
n=int(input())
a=list(map(int,input().split()))
ans=0
heapify(a)
while len(a)>=2:
    b=heappop(a)
    c=heappop(a)
    d=b+c
    ans+=d
    heappush(a,d)
print(ans)
    