# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 16:47:50 2024

@author: ghp
"""

class Disjointset:
    def __init__(self,n):
        self.father=[0]+[i for i in range(1,n+1)]
    def find(self,x):
        if self.father[x]!=x:
            self.father[x]=self.find(self.father[x])
        return self.father[x]
    def union(self,x,y):
        xset=self.find(x)
        yset=self.find(y)
        if xset==yset:
            print('Yes')
        else:
            print('No')
            self.father[yset]=xset
           
            
while True:
    try:
        n,m=map(int,input().split())
        disjset=Disjointset(n)
        for _ in range(m):
            x,y=map(int,input().split())
            disjset.union(x,y)
        ans=0
        a=[]
        for i in range(1,n+1):
            if disjset.find(i)==i:
                ans+=1
                a.append(i)
        print(ans)
        print(*a)
    except EOFError:
        break
        
        
        
    
    
    
            