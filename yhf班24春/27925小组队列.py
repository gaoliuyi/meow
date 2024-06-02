# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 09:13:42 2024

@author: ghp
"""

from collections import deque
t=int(input())
dic={}
l={}
for i in range(t):
    dic[i]=list(map(int,input().split()))
    for j in range(len(dic[i])):
        l[dic[i][j]]=i
q={}
h=[]
while True:
    s=input()
    if s=="STOP":
        break
    elif s=="DEQUEUE":
        for x in h:
            if q[x]:
                ans=q[x].popleft()
                print(ans)
                break
    else:
        a,b=s.split()
        b=int(b)
        c=l[b]
        if c in q:
            q[c].append(b)
        else:
            h.append(c)
            q[c]=deque([b])
            
            