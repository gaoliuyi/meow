# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 20:10:42 2024

@author: ghp
"""

class Tree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def buildtree(s):
    j=0
    node=nodes[j]
    for i in range(1,len(s)):
        if s[i]!='.':
            while True:
                if node.left is None:
                    node.left=Tree(s[i])
                    node=node.left
                    nodes.append(node)
                    j=nodes.index(node)
                    break
                elif node.right is None:
                    node.right=Tree(s[i])
                    node=node.right
                    nodes.append(node)
                    j=nodes.index(node)
                    break
                else:
                    j-=1
                    node=nodes[j]
        else:
            while True:
                if node.left is None:
                    node.left=Tree(s[i])
                    break
                elif  node.right is None:
                    node.right=Tree(s[i])
                    break
                else:
                    j-=1
                    node=nodes[j]
    return nodes[0]
def mpout(x):
    if x.left:
        mpout(x.left)
    if x.val!='.':
        print(x.val,end='')
    if x.right:
        mpout(x.right)
def lpout(x):
    if x.left:
        lpout(x.left)
    if x.right:
        lpout(x.right)
    if x.val!='.':
        print(x.val,end='')
s=input()
nodes=[Tree(s[0])]
x=buildtree(s)
mpout(x)
print()
lpout(x)

    
                
        
        
        
        
    