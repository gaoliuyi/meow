# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:19:08 2024

@author: ghp
"""

r=int(input())
s=0
n=int(input())
j=0
m=[0]*(r+1)
for i in range(n):
    l,t,w,h=map(int,input().split())
    for j in range(l+1,l+w+1):
        m[j]+=h
a=sum(m)
for i in range(1,r+1):
    s+=m[i]
    if s*2>=a:
        ans=i
        break
while ans<r:
    if m[ans+1]==0:
        ans+=1
    else:
        break
print(ans)

        
            