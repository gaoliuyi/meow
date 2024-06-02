# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 20:19:54 2024

@author: ghp
"""
from collections import deque
class Tree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
p=list(map(int,input().split()))
n=len(p)
nodes=[Tree(p[i]) for i in range(n)]

for i in range(1,n):
    root=nodes[0]
    while True:
        if p[i]<root.val:
            if root.left:
                root=root.left
            else:
                root.left=nodes[i]
                break
        elif p[i]>root.val:
            if root.right:
                root=root.right
            else:
                root.right=nodes[i]
                break
        else:
            break
def pout(r):
    q=deque()
    q.append(r)
    ans=[]
    while q:
        node=q.popleft()
        ans.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    print(*ans)
pout(nodes[0])

            
    
            
        