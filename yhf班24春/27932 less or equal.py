# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 21:37:24 2024

@author: ghp
"""

n,k=map(int,input().split())
s=list(map(int,input().split()))
ans=-1
if k>n:
    print(-1)
    exit()
s.sort()
if k==0:
    if s[0]==1:
        print(-1)
    else:
        print(1)
    exit()
a=s[k-1]
if s.count(a)>1:
    print(-1)
else:
    print(a)