# -*- coding: utf-8 -*-
"""
Created on Tue May 21 11:08:50 2024

@author: ghp
"""

n=int(input())
ans=[0]*(n)
num=list(map(int,input().split()))
stack=[]
for i in range(n-1,-1,-1):
    while stack and num[stack[-1]]<=num[i]:
        stack.pop()
    if stack:
        ans[i]=stack[-1]+1
    stack.append(i)
print(*ans)

