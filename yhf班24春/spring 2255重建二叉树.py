# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 11:49:51 2024

@author: ghp
"""
class Tree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def buildtree(a,b):
    nodes=[Tree(i) for i in a]
    n=len(a)
    for i in range(1,n):
        if b.index(a[i])<b.index(a[i-1]):
            nodes[i-1].left=nodes[i]
        else:
            x=b.index(a[i])
            while True:
                x-=1
                if a.index(b[x])<i:
                    nodes[a.index(b[x])].right=nodes[i]
                    break
    return nodes[0]
def pout(x):
    if x.left:
        pout(x.left)
    if x.right:
        pout(x.right)
    print(x.val,end='')
        
while True:
    try:
        a,b=input().split()
        root=buildtree(a,b)
        pout(root)
        print()
        
    except EOFError:
        break