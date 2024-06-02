# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 16:45:10 2024

@author: ghp
"""

class Node:
    def __init__(self):
        self.children={}
class Tree:
    def __init__(self):
        self.root=Node()
    def insert(self,val):
        cur=self.root
        for x in val.split('\\'):
            if x not in cur.children:
                cur.children[x]=Node()
            cur=cur.children[x]
    def dfs(self,a,depth):
        for b in sorted(a.children):
            print(' '*depth+b)
            self.dfs(a.children[b],depth+1)
s=Tree()
n=int(input())
for i in range(n):
    w=input()
    s.insert(w)
s.dfs(s.root,0)
    
    
            