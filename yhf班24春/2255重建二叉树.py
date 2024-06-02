# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 15:28:23 2024

@author: ghp
"""
cnt=0
ls=[]
rs=[]
n=[]
def solve(l,r):
    global cnt
    if cnt>len(p)-1:
        return -1
    x=p[cnt]
    y=m.find(x)
    if y<l or y>r:
        return -1
    x=n.index(x)
    cnt+=1
    ls[x]=solve(l,y-1)
    rs[x]=solve(y+1,r)
    return x
def pout(x):
    if ls[x]!=-1:
        pout(ls[x])
    if rs[x]!=-1:
        pout(rs[x])
    print(n[x],end='')
while True:
    try:
        p,m=input().split()
        n=sorted(p)
        cnt=0
        ls=[-1]*len(p)
        rs=[-1]*len(p)
        x=solve(0,len(p)-1)
        pout(x)
        print()
    except EOFError:
        break
    
    