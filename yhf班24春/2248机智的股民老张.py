# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 10:08:43 2024

@author: ghp
"""
win=0
low=0
a=list(map(int,input().split()))
n=len(a)
for i in range(0,n):
    if i==0:
        low=a[0]
    elif i<n-1:
        if a[i-1]<=a[i] and a[i]>=a[i+1]:
            win=max(a[i]-low,win)
        elif a[i-1]>=a[i] and a[i]<=a[i+1]:
            low=min(low,a[i])
    else:
        win=max(win,a[n-1]-low)
print(win)