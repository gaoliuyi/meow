# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 09:54:12 2024

@author: ghp
"""

#嵌套列表法定义的二叉树
def BinaryTree(r,left=[],right=[]):
    return [r,left,right]
#将新节点插入树中作为根的直接左右节点，原来的子节点变为新节点的子节点
def insertLeft(root,newBranch):
    root[1]=BinaryTree(newBranch,left=getLeftChild(root))
    return root
def insertRight(root,newBranch):
    root[2]=BinaryTree(newBranch,right=getRightChild(root))
    return root
#取得or返回根节点
def getRootval(root):
    return root[0]
def setRootval(root,newVal):
    root[0]=newVal
#获得左/右子树
def getLeftChild(root):
    return root[1]
def getRightChild(root):
    return root[2]
if __name__=="__main__":
    r=BinaryTree(3)
    insertLeft(r,4)
    insertLeft(r,11)
    insertLeft(r,9)
    insertRight(r,6)
    insertRight(r,7)
    print(r)