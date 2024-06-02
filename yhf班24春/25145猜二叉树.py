# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 19:16:20 2024

@author: ghp
"""
from collections import deque
class Tree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def build(a,b):
    n=len(a)
    nodes=[Tree(b[i]) for i in range(n)]
    for i in range(n-2,-1,-1):
        if a.index(b[i])>a.index(b[i+1]):
            nodes[i+1].right=nodes[i]
        else:
            x=a.index(b[i])
            while True:
                x+=1
                if b.index(a[x])>i:
                    nodes[b.index(a[x])].left=nodes[i]
                    break
                
    return nodes[-1]
def levelorder(root):
    q=deque()
    q.append(root)
    while q:
        node=q.popleft()
        print(node.val,end='')
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
t=int(input())
for i in range(t):
    a=input()
    b=input()
    root=build(a,b)
    levelorder(root)
    print()
            
            