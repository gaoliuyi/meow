# -*- coding: utf-8 -*-
"""
Created on Thu May 16 21:51:41 2024

@author: ghp
"""
ans=0
n=int(input())
h=[int(input()) for i in range(n)]
l=[-1]*n
r=[n]*n
stack=[]
for i in range(n):
    while stack and h[stack[-1]]<h[i]:
        stack.pop()
    if stack:
        l[i]=stack[-1]
    stack.append(i)
stack=[]
for i in range(n-1,-1,-1):
    while stack and h[stack[-1]]>h[i]:
        stack.pop()
    if stack:
        r[i]=stack[-1]
    stack.append(i)
for i in range(n-1,-1,-1):
    for j in range(l[i]+1,i):
        if r[j]>i:
            ans=max(ans,i-j+1)
            break
print(ans)
        
