# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 15:53:07 2024

@author: ghp
"""

class DisjSet:
    def __init__(self,n):
        self.rank=[1]*n
        self.parent=[i for i in range(n)]
    
    def union(self,x,y):
        xroot=self.find(x)
        yroot=self.find(y)
        if xroot==yroot:
            return
        
        if self.rank[xroot]<self.rank[yroot]:
            self.parent[xroot]=yroot
        elif self.rank[xroot]>self.rank[yroot]:
            self.parent[yroot]=xroot
        else:
            self.parent[yroot]=xroot
            self.rank[xroot]+=1
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    x=DisjSet(n)
    for i in range(m):
        p=list(map(int,input().split()))
        for j in range(2,p[0]+1):
            x.union(p[1],p[j])
    ans=0
    for i in range(n):
        if x.find(i)==x.find(0):
            ans+=1
    print(ans)
            
            
                
            
            