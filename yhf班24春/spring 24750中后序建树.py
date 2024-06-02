# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 22:00:28 2024

@author: ghp
"""

class Tree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def solve(a,b):
    n=len(a)
    nodes=[Tree(x) for x in b]
    for i in range(n-1,0,-1):
        if a.index(b[i-1])>a.index(b[i]):
            nodes[i].right=nodes[i-1]
        else:
            x=a.index(b[i-1])+1
            while True:
                y=b.index(a[x])
                if y>i-1:
                    nodes[y].left=nodes[i-1]
                    break
                x+=1
    return nodes[-1]
def pout(x):
    if x.val:
        print(x.val,end='')
    if x.left:
        pout(x.left)
    if x.right:
        pout(x.right)
a=input()
b=input()
root=solve(a,b)
pout(root)
            
    