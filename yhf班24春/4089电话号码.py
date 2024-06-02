# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 21:45:29 2024

@author: ghp
"""

class Tree:
    def __init__(self):
        self.child={}
class Tri:
    def __init__(self):
        self.root=Tree()
    def insert(self,num):
        curnode=self.root
        for x in num:
            if x not in curnode.child:
                curnode.child[x]=Tree()
            curnode=curnode.child[x]
    def search(self,num):
        curnode=self.root
        for x in num:
            if x not in curnode.child:
                return 0
            curnode=curnode.child[x]
        return 1
for _ in range(int(input())):
    nums=[]
    for i in range(int(input())):
        nums.append(str(input()))
    nums.sort(reverse=True)
    s=0
    t=Tri()
    for y in nums:
        s+=t.search(y)
        t.insert(y)
    if s>0:
        print('NO')
    else:
        print('YES')
        
        
    