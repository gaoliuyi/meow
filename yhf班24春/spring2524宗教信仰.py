# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 20:25:01 2024

@author: ghp
"""

class Disjset:
    def __init__(self,n):
        self.size=[1]*n
        self.parent=[i for i in range(n)]
        self.ans=n
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def Union(self,x,y):
        xset=self.find(x)
        yset=self.find(y)
        if xset==yset:
            return
        self.ans=self.ans-1
        if self.size[xset]<self.size[yset]:
            self.parent[xset]=yset
            self.size[yset]+=self.size[xset]
        elif self.size[xset]>self.size[yset]:
            self.parent[yset]=xset
            self.size[xset]+=self.size[yset]
        else:
            self.parent[yset]=self.parent[xset]
            self.size[xset]=self.size[xset]*2
c=0
while True:
    c+=1
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    disjset=Disjset(n)
    for x in range(m):
        i,j=map(int,input().split())
        disjset.Union(i-1,j-1)
    a=disjset.ans
    
    print(f'Case {c}: {a}')
            
                    
        
        
        
        