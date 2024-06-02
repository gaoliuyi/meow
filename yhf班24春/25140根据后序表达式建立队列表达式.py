# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 18:17:09 2024

@author: ghp
"""

class Tree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def buildtree(s):
    stack=[]
    for x in s:
        y=Tree(x)
        if x.isupper():
            y.right=stack.pop()
            y.left=stack.pop()
        stack.append(y)
    return stack[0]

def levelorder(root):
    q=[root]
    ans=[]
    while q:
        node=q.pop(0)
        ans.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return ans
for i in range(int(input())):
    s=input()
    root=buildtree(s)
    ans=levelorder(root)
    ans.reverse()
    print(''.join(ans))

        
        
        
    
    
        
        
      
      
            
            
        