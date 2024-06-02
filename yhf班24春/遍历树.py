# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 09:44:33 2024

@author: ghp
"""
tree={}
nodes=[]
child=set()
n=int(input())
for i in range(n):
    s=list(map(int,input().split()))
    a=s[0]
    if len(s)>1:
        
        for i in s[1:]:
            child.add(i)
        s.sort()
        nodes.append(a)
        tree[a]=s
    else:
        nodes.append(a)
for x in nodes:
    if x not in child:
        root=x
        break
def pout(x):
    if x not in tree:
        print(x)
        return
    for y in tree[x]:
        if y==x:
            print(x)
        else:
            pout(y)
pout(root)
    
    
    
    
    
    