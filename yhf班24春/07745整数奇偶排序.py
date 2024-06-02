# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 22:03:32 2024

@author: ghp
"""

l=list(map(int,input().split()))
a=[]
b=[]
for i in range(len(l)):
    if l[i]%2==0:
        b.append(l[i])
    else:
        a.append(l[i])
a.sort(reverse=True)
b.sort()
c=a+b
print(*c)