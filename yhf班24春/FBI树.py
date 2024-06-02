# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 21:46:09 2024

@author: ghp
"""

class Node:
    def __init__(self):
        self.val=None
        self.left=None
        self.right=None
def buildtree(s):
    node=Node()
    if '0' in s and '1' in s:
        node.val='F'
    elif '0' in s:
        node.val='B'
    elif '1' in s:
        node.val='I'
    if len(s)>1:
        n=len(s)
        s1=s[:n//2]
        s2=s[n//2:]
        node.left=buildtree(s1)
        node.right=buildtree(s2)
    return node
def pout(x):
    if x is not None:
        pout(x.left)
        pout(x.right)
        print(x.val,end='')
l=int(input())
s=input()
root=buildtree(s)
pout(root)
    
       