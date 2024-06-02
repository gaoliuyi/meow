# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 10:11:54 2024

@author: ghp
"""

a=input()
n=len(a)
ans=[0]*n
num=0
for i in range(n):
    num=num*2+int(a[i])
    if num%5:
        ans[i]=0
    else:
        ans[i]=1
print(''.join(map(str,ans)))