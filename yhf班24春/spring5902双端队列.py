# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 18:15:22 2024

@author: ghp
"""

from collections import deque
for _ in range(int(input())):
    q=deque()
    for i in range(int(input())):
        a,b=map(int,input().split())
        if a==1:
            q.append(b)
        if a==2:
            if q:
                if b==0:
                    q.popleft()
                elif b==1:
                    q.pop()
    if q:
        print(*q)
    else:
        print('NULL')