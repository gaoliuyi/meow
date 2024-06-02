# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 17:25:25 2024

@author: ghp
"""

ans=0

class Disjointset:
    def __init__(self,n):
        self.father=[0]+[i for i in range(1,n+1)]
    def find(self,x):
        if self.father[x]!=x:
            self.father[x]=self.find(self.father[x])
        return self.father[x]
    def union(self,x,y):
        global ans
        xset=self.find(x)
        yset=self.find(y)
        if xset==yset:
            print('Yes')
        else:
            print('No')
            self.father[yset]=xset
            ans+=1
            v.add(yset)
            
while True:
    try:
        n,m=map(int,input().split())
        ans=0
        v=set()
        v.add(0)
        disjset=Disjointset(n)
        for _ in range(m):
            x,y=map(int,input().split())
            disjset.union(x,y)
        print(n-ans)
        a=[i for i in range(1,n+1) if i not in v]
        print(*a)
    except EOFError:
        break