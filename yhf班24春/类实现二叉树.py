# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:38:31 2024

@author: ghp
"""

class BinaryTree:
    def __init__(self,rootObj):
        self.key=rootObj
        self.leftChild=None
        self.rightChild=None
    def insertLeft(self,newNode):
        self.leftChild=BinaryTree(newNode,left=self.leftChild)
    def insertRight(self,newNode):
        self.rightChild=BinaryTree(newNode,right=self.rightChild)
    def getRightChild(self):
        return self.rightChild
    def getLeftChild(self):
        return self.leftChild
    def setRootVal(self,obj):
        self.key=obj
    def getRootVal(self):
        return self.key
def preorder(tree):
    if tree:
        print(tree.getRootVal)
        preorder(tree.getLeftChild)
        preorder(tree.getRightChild)
        
    