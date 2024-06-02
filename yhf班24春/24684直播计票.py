# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 09:49:00 2024

@author: ghp
"""

from collections import defaultdict
vote=defaultdict(int)
a=list(map(int,input().split()))
for i in range(len(a)):
    vote[a[i]]+=1
m=max(vote.values())
ans=[]
for i in vote.items():
    if i[1]==m:
        ans.append(i[0])
ans.sort()
print(*ans)