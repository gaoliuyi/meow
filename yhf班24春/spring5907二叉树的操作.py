# -*- coding: utf-8 -*-
"""
Created on Thu May  2 21:09:56 2024

@author: ghp
"""

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def buildtree(t):
    nodes=[Node(i) for i in range(n)]
    for x,y,z in t:
        if y!=-1:
            nodes[x].left=nodes[y]
        if z!=-1:
            nodes[x].right=nodes[z]
    return nodes
def swap(x,y):
    for node in nodes:
        if node.left and node.left.val in [x,y]:
            node.left=nodes[y] if node.left.val==x else nodes[x]
        if node.right and node.right.val in [x,y]:
            node.right=nodes[y] if node.right.val==y else nodes[x]
def ask(node):
    while node and node.left:
        node=node.left
    return node.val
for _ in range(int(input())):
    n,m=map(int,input().split())
    t=[list(map(int,input().split())) for _ in range(n)]
    nodes=buildtree(t)
    for _ in range(m):
        k=list(map(int,input().split()))
        if k[0]==1:
            swap(k[1],k[2])
        elif k[0]==2:
            print(ask(nodes[k[1]]))