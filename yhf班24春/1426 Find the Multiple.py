# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 11:29:10 2024

@author: ghp
"""
from collections import deque
while True:
    n=int(input())
    if n==0:
        break
    q=deque()
    q.append((1,'1'))
    vis={1}
    while q:
        res,num=q.popleft()
        for i in range(2):
            num+=str(i)
            res=(res*10+i)%n
            if res==0:
                print(num)
                break
            else:
                if res not in vis:
                    vis.add(res)
                    q.append((res,num))
                
                
    