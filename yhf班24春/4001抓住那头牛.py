# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 17:27:26 2024

@author: ghp
"""

from collections import deque
q=deque()
n,k=map(int,input().split())
q.append((0,n))
v=[0]*(100001)
while q:
    t,x=q.popleft()
    v[x]=1
    if x==k:
        print(t)
        break
    for i in range(3):
        if i==0:
            nx=x-1
        elif i==1:
            nx=x+1
        else:
            nx=2*x
        if 0<=nx<=1e5 and v[nx]==0:
            
            q.append((t+1,nx))
            
            
    
    
    
    