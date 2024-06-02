# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:17:51 2024

@author: ghp
"""

n,m=map(int,input().split())
for i in range(m):
    a,b=map(int,input().split())
print(n*(n-1)//2-m)