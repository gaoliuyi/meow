# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 10:30:13 2024

@author: ghp
"""

class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def insertbst(root,val):
    if root is None:
        return Node(val)
    if val<root.val:
        root.left=insertbst(root.left,val)
    elif val>root.val:
        root.right=insertbst(root.right,val)
    return root
def preorderprint(root):
    return [root.val]+preorderprint(root.left)+preorderprint(root.right) if root else []
l=list(map(int,input().split()))
bstroot=None
for num in l:
    bstroot=insertbst(bstroot,num)
ans=preorderprint(bstroot)
print(*ans)

    
    