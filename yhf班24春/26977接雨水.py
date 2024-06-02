# -*- coding: utf-8 -*-
"""
Created on Thu May 30 09:42:59 2024

@author: ghp
"""

n=int(input())
num=list(map(int,input().split()))
stack=[]
ans=0
minh=0
h=0
for i in range(n-1,-1,-1):
    while stack and num[stack[-1]]<num[i]:
        h=num[stack[-1]]
        stack.pop()
        if not stack:
            break
        minh=min(num[i],num[stack[-1]])
        d=stack[-1]-i-1
        ans+=(minh-h)*d
    stack.append(i)
print(ans)
        