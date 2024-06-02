# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 19:43:52 2024

@author: ghp
"""

class Tree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
n=int(input())
nodes=[Tree(i) for i in range(1,n+1)]
p=list(map(int,input().split()))
root=nodes[p[0]-1]
for j in range(1,n):
    root=nodes[p[0]-1]
    while True:
        if p[j]<root.val:
            if root.left:
                root=root.left
            else:
                root.left=nodes[p[j]-1]
                break
        else:
            if root.right:
                root=root.right
            else:
                root.right=nodes[p[j]-1]
                break
def pout(x):
    if x.left:
        pout(x.left)
    if x.right:
        pout(x.right)
    if x.val:
        print(x.val,end=' ')
pout(nodes[p[0]-1])
    
