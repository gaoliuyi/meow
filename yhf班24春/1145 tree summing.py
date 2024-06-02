# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 22:27:14 2024

@author: ghp
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:39:07 2024

@author: ghp
"""
#tree class
class Treenode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=None
        self.right=None
#calculate sum
def find_path(root,targetsum):
    if root is None:
        return False
    elif root.left is None and root.right is None:
        return root.val==targetsum
    leftexist=find_path(root.left,targetsum-root.val)
    rightexist=find_path(root.right,targetsum-root.val)
    return leftexist or rightexist
#build a tree
def buildtree(s):
    stack=[]
    i=0
    while i<len(s):
        if s[i].isdigit() or s[i]=='-':
            j=i
            while j<len(s) and (s[j].isdigit() or s[j]=='-'):
                j+=1
            num=int(s[i:j])
            node=Treenode(num)
            if stack:
                parent=stack[-1]
                if parent.left is None:
                    parent.left=node
                else:
                    parent.right=node
            stack.append(node)
            i=j
        elif s[i]=='[':
            i+=1
        elif s[i]==']' and s[i-1]!='[' and len(stack)>1:
            stack.pop()
            i+=1
        else:
            i+=1
    return stack[0] if len(stack)>0 else None
while True:
    try:
        s=input()
    except:
        break
    s=s.split()
    targetsum=int(s[0])
    tree=('').join(s[1:])
    tree=tree.replace('(',',[').replace(')',']')
    while True:
        try:
            tree=eval(tree[1:])
            break
        except SyntaxError:
            s=input().split()
            s=('').join(s)
            s=s.replace('(',',[').replace(')',']')
            tree+=s
    tree=str(tree)
    tree=tree.replace(',[','[')
    if tree=='[]':
        print('no')
        continue

    root=buildtree(tree)
    if find_path(root,targetsum):
        print('yes')
    else:
        print('no')