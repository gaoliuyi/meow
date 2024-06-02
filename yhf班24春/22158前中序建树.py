# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 21:32:08 2024

@author: ghp
"""

class Tree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def solve(a,b):
    nodes=[Tree(x) for x in a]
    n=len(a)
    for i in range(1,n):
        if b.index(a[i])<b.index(a[i-1]):
            nodes[i-1].left=nodes[i]
        else:
             x=b.index(a[i])-1
             while True:
                 y=a.index(b[x])
                 if a.index(b[x])<i:
                     nodes[y].right=nodes[i]
                     break
                 x-=1
    return nodes[0]
def pout(root):
    if root.left:
        pout(root.left)
    if root.right:
        pout(root.right)
    if root.val:
        print(root.val,end='')
while True:
    try:
        a=input()
        b=input()
        root=solve(a,b)
        pout(root)
        print()
    except EOFError:
        break
    
    
    

    
    