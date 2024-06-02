# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 11:35:39 2024

@author: ghp
"""
def compute(m,n):
    depth=1
    while m*depth<=n:
        depth*=2
    return min(depth-1,n-(depth//2)*(m-1))
while True:
    m,n=map(int,input().split())
    if (m,n)!=(0,0):
        print(compute(m,n))
    else:
        break