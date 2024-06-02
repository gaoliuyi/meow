# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 17:39:34 2024

@author: ghp
"""

n,m=map(int,input().split())
a=list(map(int,input().split()))
for i in range(m):
    x,y=input().split()
    if x=='Q':
        ans=0
        for j in range(n):
            z=bin(a[j])
            
            if z[len(z)-int(y)-1]=='1':
                ans+=1
        print(ans)
    elif x=="C":
        for j in range(n):
            a[j]+=int(y)
        