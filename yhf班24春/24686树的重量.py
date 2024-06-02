# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 20:21:39 2024

@author: ghp
"""

k,n=map(int,input().split())
t=1<<k
f=[0]*t;g=[0]*t;d=[0]*t
for i in range(t-1,0,-1):
    d[i]=1 if 2*i>t-1 else d[i<<1]+1
for _ in range(n):
    a=list(map(int,input().split()))
    if len(a)==2:
        u=a[1]
        s=f[1]
        while u!=1:
            s+=f[u]
            u>>=1
        ans=s*((1<<d[a[1]])-1)+g[a[1]]
        print(ans)
    elif len(a)==3:
        u=a[1]
        w=a[2]*((1<<d[u])-1)
        f[u]+=a[2]
        while u!=1:
            u>>=1
            g[u]+=w
            
        
    
    
        