# -*- coding: utf-8 -*-
"""
Created on Sat May 11 08:35:23 2024

@author: ghp
"""

a=input()
n=len(a)
ans=[0]*n
num=0
for i in range(n):
    num=num*2+int(a[i])
    if num%5==0:
        ans[i]=1
print("".join(map(str,ans)))
