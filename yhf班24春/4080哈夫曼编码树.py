# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 20:53:36 2024

@author: ghp
"""
from heapq import heappop,heappush,heapify
n=int(input())
ans=0
p=list(map(int,input().split()))
heapify(p)
while len(p)>1:
    a=heappop(p)
    b=heappop(p)
    c=a+b
    ans+=c
    heappush(p,c)
print(ans)    


    