# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:54:51 2024

@author: ghp
"""
from collections import deque
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
n=int(input())
nodes=[Node(i) for i in range(n+1)]
for i in range(1,n+1):
    a,b=map(int,input().split())
    if a!=-1:
        nodes[i].left=nodes[a]
    if b!=-1:
        nodes[i].right=nodes[b]
def bfs():
    ans=[]
    q=deque()
    h=0
    q.append((1,0))
    while q:
        x,y=q.popleft()
        if not q or q[0][1]!=h:
            ans.append(x)
            h+=1
        c=nodes[x]
        if c.left:
            q.append((c.left.val,y+1))
        if c.right:
            q.append((c.right.val,y+1))
    return ans
ans=bfs()
print(*ans)