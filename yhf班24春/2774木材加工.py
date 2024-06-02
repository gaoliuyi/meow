# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 17:25:30 2024

@author: ghp
"""

def check(x):
    s=0
    for i in arr:
        s+=i//x
    if s>=k:
        return True
    else:
        return False
n,k=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(int(input()))
lo=0
hi=max(arr)+1
if sum(arr)<k:
    print(0)
    exit()
while lo<hi:
    mid=(lo+hi)//2
    if check(mid):
        lo=mid+1
    else:
        hi=mid
print(lo-1)
    