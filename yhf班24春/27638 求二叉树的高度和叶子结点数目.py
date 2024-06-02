# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 16:23:37 2024

@author: ghp
"""

class Tree:
    def __init__(self,left=None,right=None):
        self.left=left
        self.right=right

def height(node):
    if node is None:
        return -1
    return max(height(node.left),height(node.right))+1

def leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return leaves(node.left)+leaves(node.right)
n=int(input())   
nodes=[Tree() for i in range(n)] 
father=[-1]*n
for i in range(n):
    left,right=map(int,input().split())
    if left!=-1:
        nodes[i].left=nodes[left]
        father[left]=i
    if right!=-1:
        nodes[i].right=nodes[right]
        father[right]=i
root=father.index(-1)
print(height(nodes[root]),leaves(nodes[root]))
