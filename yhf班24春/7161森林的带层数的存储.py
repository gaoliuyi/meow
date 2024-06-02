# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 19:21:48 2024

@author: ghp
"""
from collections import deque
class Tree:
    def __init__(self,val):
        self.val=val
        self.child=[]
def buildtree(t):
    nodes=[Tree(t[i]) for i in range(0,len(t)-1,2)]
    r=(0,t[0],t[1])
    q=deque()
    q.append(r)
    i=2
    while q:
        a,b,c=q.popleft()
        c=int(c)
        if c!=0:
            for j in range(i,i+2*c,2):
                x=t[j]
                y=int(t[j+1])
                nodes[a>>1].child.append(nodes[j>>1])
                if y!=0:
                    q.append([j,x,y])
            i=i+2*c
    return nodes[0]
def lastorder(r):
    if r.child:
        for x in r.child:
            lastorder(x)
    print(r.val,end=' ')
n=int(input())
for i in range(n):
    t=list(input().split())
    k=buildtree(t)#特别注意不能重新写类否则孩子列表将被初始化覆盖
    lastorder(k)
    
    
                
                