# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:33:36 2024

@author: ghp
"""
from heapq import *
def minum(data):
    minh=[]
    maxh=[]
    ans=[]
    for i,num in enumerate(data):
        if not maxh or num>=maxh[0]:
            heappush(maxh,num)
        else:
            heappush(minh,-num)
        if len(maxh)-len(minh)>1:
            heappush(minh,-heappop(maxh))
        elif len(minh)>len(maxh):
            heappush(maxh,-heappop(minh))
        if i%2==0:
            ans.append(maxh[0])
    return ans
t=int(input())
for _ in range(t):
    data=list(map(int,input().split()))
    ans=minum(data)
    print(len(ans))
    print(*ans)
    
        