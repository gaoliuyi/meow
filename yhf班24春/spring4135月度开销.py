# -*- coding: utf-8 -*-
"""
Created on Tue May 21 18:54:50 2024

@author: ghp
"""

expense=[]
n,m=map(int,input().split())
for i in range(n):
    expense.append(int(input()))
def check(x):
    s=0
    num=1
    for i in range(n):
        s=s+expense[i]
        if s>x:
            num+=1
            s=expense[i]
    if num>m:
        return False
    else:
        return True
lo=max(expense)
hi=sum(expense)
while lo<hi:
    a=(lo+hi)//2
    if check(a):
        hi=a
    else:
        lo=a+1
print(lo)