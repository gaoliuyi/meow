# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 22:01:50 2024

@author: ghp
"""

class Binheap:
    def  __init__(self):
        self.hlist=[0]
        self.size=0
    def percup(self,i):
        while i//2>0:
            if self.hlist[i]<self.hlist[i//2]:
                self.hlist[i],self.hlist[i//2]=self.hlist[i//2],self.hlist[i]
            i=i//2
    def insert(self,k):
        self.hlist.append(k)
        self.size=self.size+1
        self.percup(self.size)
    def percdown(self,i):
        while (i*2)<=self.size:
            mc=self.minchild(i)
            if self.hlist[i]>self.hlist[mc]:
                self.hlist[i],self.hlist[mc]=self.hlist[mc],self.hlist[i]
            i=mc
    def minchild(self,i):
        if i*2+1>self.size:
            return i*2
        else:
            if self.hlist[i*2]<self.hlist[i*2+1]:
                return i*2
            else:
                return i*2+1
    def delmin(self):
        ans=self.hlist[1]
        self.hlist[1]=self.hlist[self.size]
        self.hlist.pop()
        self.size=self.size-1
        self.percdown(1)
        return ans
bh=Binheap()
for i in range(int(input())):
    a=list(map(int,input().split()))
    if a[0]==1:
        bh.insert(a[1])
    else:
        print(bh.delmin())
        