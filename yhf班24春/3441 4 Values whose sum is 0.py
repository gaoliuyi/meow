# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:40:42 2024

@author: ghp
"""

n=int(input())
a,b,c,d=[0]*n,[0]*n,[0]*n,[0]*n
for i in range(n):
    a[i],b[i],c[i],d[i]=map(int,input().split())
di={}
for i in range(n):
    for j in range(n):
        if a[i]+b[j] not in di:
            di[a[i]+b[j]]=0
        di[a[i]+b[j]]+=1
ans=0
for i in range(n):
    for j in range(n):
        if -(c[i]+d[j]) in di:
            ans+=di[-(c[i]+d[j])]
print(ans)
            