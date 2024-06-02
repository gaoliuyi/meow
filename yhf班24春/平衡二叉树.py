# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 14:54:29 2024

@author: ghp
"""

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.h=1
class AVL:
    def __init__(self):
        self.root=None
    def insert1(self,value):
        if not self.root:
            self.root=Node(value)
        else:
            self.root=self.insert(value,self.root)
    def insert(self,value,node):
        if not node:
            return Node(value)
        elif value<node.value:
            node.left=self.insert(value,node.left)
        else:
            node.right=self.insert(value,node.right)
        node.h=max(self.geth(node.left),self.geth(node.right))+1
        
        b=self.getb(node)
        if b>1:
            if value<node.left.value:
                return self.rrotate(node)
            else:
                node.left=self.lrotate(node.left)
                return self.rrotate(node)
        if b<-1:
            if value>node.right.value:
                return self.lrotate(node)
            else:
                node.right=self.rrotate(node.right)
                return self.lrotate(node)
        return node
    def geth(self,node):
        if not node:
            return 0
        return node.h
    def getb(self,node):
        if not node:
            return 0
        return self.geth(node.left)-self.geth(node.right)
    def lrotate(self,z):
        y=z.right
        t=y.left
        y.left=z
        z.right=t
        z.h=max(self.geth(z.left),self.geth(z.right))+1
        y.h=max(self.geth(y.left),self.geth(y.right))+1
        return y
    def rrotate(self,z):
        y=z.left
        t=y.right
        y.right=z
        z.left=t
        z.h=max(self.geth(z.left),self.geth(z.right))+1
        y.h=max(self.geth(y.left),self.geth(y.right))+1
        return y
    def preorder(self,root):
        if not root:
            return []
        return [root.value]+self.preorder(root.left)+self.preorder(root.right)
n=int(input())
s=list(map(int,input().split()))
avl=AVL()
for x in s:
    avl.insert1(x)
root=avl.root
ans=avl.preorder(root)
print(*ans)
        
    
    
    
    
    
    
    
    
        