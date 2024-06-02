# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 17:07:51 2024

@author: ghp
"""
import math
def check(x):
    s=0
    for y in arr:
        s+=math.ceil(y/x)
    if s<=t:
        return True
    else:
        return False
arr=list(map(int,input().split(',')))
t=int(input())
lo=sum(arr)//t
hi=sum(arr)//t+len(arr)+1
while lo<hi:
    mid=(lo+hi)//2
    if check(mid):
        hi=mid
    else:
        lo=mid+1
print(lo)