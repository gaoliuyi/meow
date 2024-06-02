# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 15:30:38 2024

@author: ghp
"""

class Tree:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
def buildtree(s):
    stack=[]
    node=None
    for x in s:
        if x.isalpha():
            node=Tree(x)
            if stack:
                if stack[-1].left:
                    stack[-1].right=node
                else:
                    stack[-1].left=node
        elif x=="(":
            if node:
                stack.append(node)
                node=None
        elif x==")":
            if stack:
                node=stack.pop()
        elif x=="*":
            node=Tree(x)
            if stack:
                if stack[-1].left:
                    stack[-1].right=node
                else:
                    stack[-1].left=node
    return node
def preorder(node):
    if node.value!='*':
        print(node.value,end='')
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)
def morder(node):
    if node.left:
        morder(node.left)
    if node.value!='*':
        print(node.value,end='')
    if node.right:
        morder(node.right)
for _ in range(int(input())):
    s=input()
    node=buildtree(s)
    preorder(node)
    print()
    morder(node)
    print()

        
        
             
            