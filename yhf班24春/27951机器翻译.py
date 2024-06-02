# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 21:28:16 2024

@author: ghp
"""

from collections import deque
m,n=map(int,input().split())
l=0
ans=0
q=deque()
s=list(input().split())
for i in range(n):
    if s[i] not in q:
        ans+=1
        q.append(s[i])
        l+=1
    if l>m:
        q.popleft()
        l-=1
print(ans)
