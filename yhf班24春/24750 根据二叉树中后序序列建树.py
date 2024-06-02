# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 10:02:07 2024

@author: ghp
"""

class Tree:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
a=input()
b=input()
n=len(a)
node=[0]*n
node[0]=Tree(b[0])
for i in range(n-1,0,-1):
    node[i]=Tree(b[i])
for i in range(n-1,0,-1):
    if a.find(b[i-1])>a.find(b[i]):
        node[i].right=node[i-1]
    else:
        x=a.find(b[i-1])
        while True:
            x+=1
            if b.find(a[x])>i-1:
                node[b.find(a[x])].left=node[i-1]
                break
        
def pout(x):
    if x.val:
        print(x.val,end='')
    if x.left:
        pout(x.left)
    if x.right:
        pout(x.right)
pout(node[n-1])
        