# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 15:05:45 2024

@author: ghp
"""

class Node:
    def __init__(self,val=0):
        self.val=val
        self.left=None
        self.right=None
def buildtree(nodesinfo):
    nodes=[Node(i) for i in range(n)]
    for val,x,y in nodesinfo:
        if x!=-1:
            nodes[val].left=nodes[x]
        if y!=-1:
            nodes[val].right=nodes[y]
    return nodes
def swapnode(nodes,x,y):
    for node in nodes:
        if node.left and node.left.val in [x,y]:
            node.left=nodes[y] if node.left.val==x else nodes[x]
        if node.right and node.right.val in [x,y]:
            node.right=nodes[y] if node.right.val==x else nodes[x]
def askleft(node):
    while node and node.left:
        node=node.left
    return node.val 
for _ in range(int(input())):
    n,m=map(int,input().split())
    nodesinfo=[tuple(map(int,input().split())) for i in range(n)]
    nodes=buildtree(nodesinfo)
    for i in range(m):
        l=list(map(int,input().split()))
        if l[0]==1:
            swapnode(nodes,l[1],l[2])
        elif l[0]==2:
            print(askleft(nodes[l[1]]))
            
        
        
    