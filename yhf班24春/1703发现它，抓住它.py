# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:08:39 2024

@author: ghp
"""
p=[]
def find(x):
    if p[x]==x:
        return x
    else:
        p[x]=find(p[x])
        return p[x]
for _ in range(int(input())):
    n,m=map(int,input().split())
    p=[i for i in range(2*n+1)]
    for i in range(m):
        s=input().split()
        b=int(s[1])
        c=int(s[2])
        if s[0]=='D':
            
            p[find(b+n)]=find(c)
            p[find(b)]=find(c+n)
        elif s[0]=="A":
            if find(b)==find(c):
                print('In the same gang.')
            elif find(b)==find(c+n) or find(c)==find(b+n):
                print('In different gangs.')
            else:
                print('Not sure yet.')
            
                
            
            
    