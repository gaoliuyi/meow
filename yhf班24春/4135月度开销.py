# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:01:45 2024

@author: ghp
"""

n,m=map(int,input().split())
ex=[]
for i in range(n):
    ex.append(int(input()))

def check(x):
    s=0
    i=0
    num=0
    while i<n:
        s+=ex[i]
        if s>x:
            s=ex[i]
            num+=1
        i+=1
    if num>=m:
        return False
    else:
        return True
def binary_search():
    lo=max(ex)
    hi=sum(ex)
    while lo<hi:
        mid=(lo+hi)//2
        if check(mid):
            hi=mid
        else:
            lo=mid+1
    return lo
print(binary_search())
        