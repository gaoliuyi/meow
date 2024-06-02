# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 16:44:27 2024

@author: ghp
"""
class Tree:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
a=input()
n=len(a)
nodes=[Tree(a[i]) for i in range(n)]
for i in range(1,n):
    j=i
    while True:
        j-=1
        if nodes[j].val!='.':
            if nodes[j].left==None:
                nodes[j].left=nodes[i]
                break
            elif nodes[j].right==None:
                nodes[j].right=nodes[i]
                break
def pout(x):
    if x.val!='.':
        pout(x.left)
        print(x.val,end='')
        pout(x.right)
def poutt(x):
    if x.val!='.':
        poutt(x.left)
        poutt(x.right)
        print(x.val,end='')
pout(nodes[0])
print()
poutt(nodes[0])
        
        
    
