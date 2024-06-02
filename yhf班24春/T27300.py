# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 19:50:14 2024

@author: ghp
"""

n=int(input())
dic={}
m=[]
for i in range(n):
    a,b=input().split('-')
    if b[-1]=='B':
        c=float(b[:-1])*1000
    else:
        c=float(b[:-1])
    if a in dic:
        dic[a].append([c,b])
    else:
        dic[a]=[[c,b]]
        m.append(a)
m.sort()
for i in m:
    dic[i].sort()
    print(i,end=': ')
    e=[]
    for j in dic[i]:
        e.append(j[1])
    print(', '.join(e))
        