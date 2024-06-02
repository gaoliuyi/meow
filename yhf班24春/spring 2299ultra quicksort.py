# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 21:58:48 2024

@author: ghp
"""
from bisect import *
while True:
    n=int(input())
    if n==0:
        break
    a=[]
    res=0
    for i in range(n):
        num=int(input())
        res+=bisect_left(a,num)
        insort_left(a,num)
    ans=n*(n-1)//2-res
    print(ans)