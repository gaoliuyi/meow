# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 16:17:37 2024

@author: ghp
"""
from collections import deque
class Node:
    def __init__(self,val):
        self.val=val
        self.children=[]
def buildtree(i):
    node=Node('')
    node.val=l[i][0]
    if l[i][1]=='0' and l[i][0]!="$":
        i+=1
        child,i=buildtree(i)
        node.children.append(child)
        i+=1
        child,i=buildtree(i)
        node.children.append(child)
    return node,i
def printtree(x):
    p=deque()
    q=deque()
    while x is not None:
        if x.val!="$":
            p.append(x)
        x=x.children[1] if len(x.children)>1 else None
    while p:
        q.append(p.pop())
    while q:
        x=q.popleft()
        print(x.val,end=' ')
        if x.children:
            x=x.children[0]
            while x is not None:
                if x.val!="$":
                    p.append(x)
                x=x.children[1] if len(x.children)>1 else None
        while p:
            q.append(p.pop())
n=int(input())
l=input().split(' ')
root,i=buildtree(0)
printtree(root)