# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:24:15 2024

@author: ghp
"""

n=int(input())
v=list(map(int,input().split()))
tree=[0]*(n+1)
def lowbit(x):
    return x&-x
def update(x,y):
    while x<=n:
        tree[x]+=y
        x+=lowbit(x)
def getsum(x):
    tot=0
    while x:
        tot+=tree[x]
        x-=lowbit(x)
    return tot
ans=0
keys=sorted(v)
dic={}
for i in range(n):
    dic[keys[i]]=i+1

for i in range(n):
    cnt=getsum(dic[v[i]])
    update(dic[v[i]],1)
    ans+=cnt
print(ans)
    
    
    