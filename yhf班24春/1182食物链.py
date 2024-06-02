# -*- coding: utf-8 -*-
"""
Created on Wed May 22 09:08:51 2024

@author: ghp
"""
n,k=map(int,input().split())
p=[i for i in range(3*n+1)]
def find(x):
    if p[x]==x:
        return x
    else:
        p[x]=find(p[x])
        return p[x]
ans=0
for i in range(k):
    t,x,y=map(int,input().split())
    if x>n or y>n:
        ans+=1
        continue
    if t==1:
        if find(x+n)==find(y) or find(y+n)==find(x):
            ans+=1
            continue
        p[find(x)]=find(y)
        p[find(x+n)]=find(y+n)
        p[find(x+2*n)]=find(y+2*n)
    else:
        if find(x)==find(y) or find(x)==find(y+n):
            ans+=1
            continue
        p[find(x+n)]=find(y)
        p[find(x+2*n)]=find(y+n)
        p[find(x)]=find(y+2*n)
print(ans)
    
        
        