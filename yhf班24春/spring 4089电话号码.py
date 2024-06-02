# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:04:47 2024

@author: ghp
"""

class Tree:
    def __init__(self):
        self.child={}
class Tri:
    def __init__(self):
        self.root=Tree()
    def add(self,num):
        node=self.root
        for x in num:
            if x not in node.child:
                node.child[x]=Tree()
            node=node.child[x]
    def search(self,num):
        node=self.root
        for x in num:
            if x not in node.child:
                return 0
            node=node.child[x]
        return 1
for i in range(int(input())):
    t=[]
    for j in range(int(input())):
        t.append(list(input()))
    t.sort(reverse=True)
    tri=Tri()
    s=0
    for num in t:
        s+=tri.search(num)
        if s>0:
            print('NO')
            break
            
        tri.add(num)
        
    else:
        print('YES')
            