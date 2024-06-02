# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:49:26 2024

@author: ghp
"""

class Tree:
    def __init__(self,val):
        self.val=val
        self.children=[]
def buildtree(t):
    if len(t)==1:
        k=Tree(t[0])
        return k
    stack=[]
    a=None
    for x in t:
        if x.isalpha():
            a=Tree(x)
            if stack:
                stack[-1].children.append(a)
        elif x=='(':
            if a:
                stack.append(a)
            a=None
        elif x==')':
            root=stack.pop()
    return root
def preorder(root):
    print(root.val,end='')
    if root.children:
        for x in root.children:
            preorder(x)
def lastorder(root):
    if root.children:
        for x in root.children:
            lastorder(x)
    print(root.val,end='')
t=input()
root=buildtree(t)
preorder(root)
print()
lastorder(root)
            
        