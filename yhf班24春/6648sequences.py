# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 16:07:11 2024

@author: ghp
"""
from heapq import heappush,heappop
def solve(s1,s2,n):
    s1.sort()
    s2.sort()
    result=[]
    nowmin=[]
    
    for i in range(n):
        heappush(nowmin,(s1[0]+s2[i],0,i))
    while nowmin and n>0:
        nowm,j,i=heappop(nowmin)
        result.append(nowm)
        if j+1<len(s1):
            heappush(nowmin,(s1[j+1]+s2[i],j+1,i))
        n-=1
    return result
for _ in range(int(input())):
    m,n=map(int,input().split())
    seqs=[list(map(int,input().split())) for i in range(m)]
    for seq in seqs:
        seq.sort()
    currentmin=seqs[0]
    for i in range(1,m):
        currentmin=solve(currentmin,seqs[i],n)
    print(*currentmin)