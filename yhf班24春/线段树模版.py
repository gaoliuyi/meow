# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 11:26:56 2024

@author: ghp
"""

a=list(map(int,input().split()))
n=len(a)
tree=[0]*(2*n)
# fuction to build the tree
def build(arr):
    # insert leaf node to the tree
    for i in range(n):
        tree[n+i]=arr[i]
    # calculating parents
    for i in range(n-1,0,-1):
        tree[i]=tree[i<<1]+tree[i<<1|1]
# function to update a tree node
def updateTreeNode(p,value):
    # set value at position p
    tree[p+n]=value
    p=p+n
    
    # move upward and update parents
    i=p
    while i>1:
        tree[i>>1]=tree[i]+tree[i^1]
        i>>=1
#function to get sum on interval [l,r)
def query(l,r):
    res=0
    #loop to find sum in the range
    l+=n
    r+=n
    while l<r:
        if (l&1):
            res+=tree[l]
            l+=1
        if (r&1):
            r-=1
            res+=tree[r]
        l>>=1
        r>>=1
    return res
            
        
    
    
