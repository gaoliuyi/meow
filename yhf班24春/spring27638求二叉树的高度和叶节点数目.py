# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:33:10 2024

@author: ghp
"""

class Tree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
n=int(input())
nodes=[Tree(i) for i in range(n)]
father=[-1]*n
for i in range(n):
    a,b=map(int,input().split())
    if a!=-1:
        nodes[i].left=nodes[a]
        father[a]=i
    if b!=-1:
        nodes[i].right=nodes[b]
        father[b]=i
def h(root):
    if root is None:
        return -1
    return max(h(root.left),h(root.right))+1
def l(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return l(root.left)+l(root.right)
root=father.index(-1)
print(h(nodes[root]),l(nodes[root]))
        
        
    
