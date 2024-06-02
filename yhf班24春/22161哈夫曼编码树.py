# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:15:07 2024

@author: ghp
"""

from heapq import heappop,heappush
class Tree:
    def __init__(self,weight,char=None):
        self.weight=weight
        self.char=char
        self.left=None
        self.right=None
    def __lt__(self,other):
        if self.weight==other.weight:
            return self.char<other.char
        return self.weight<other.weight
def buildtree(c):
    h=[]
    for char,weight in c.items():
        heappush(h,Tree(weight,char))
    while len(h)>1:
        left=heappop(h)
        right=heappop(h)
        root=Tree(left.weight+right.weight,min(left.char,right.char))
        root.left=left
        root.right=right
        heappush(h,root)
    return h[0]
def encode(root):
    codes={}
    def tran(node,code):
        if node.left is None and node.right is None:
            codes[node.char]=code
        else:
            tran(node.left,code+'0')
            tran(node.right,code+'1')
    tran(root,'')
    return codes
def encoding(codes,s):
    code=''
    for char in s:
        code+=codes[char]
    return code
def decoding(root,c):
    decode=''
    node=root
    for bit in c:
        if bit=='0':
            node=node.left
        else:
            node=node.right
        if node.left is None and node.right is None:
            decode+=node.char
            node=root
    return decode
n=int(input())
c={}
for i in range(n):
    ch,w=input().split()
    c[ch]=int(w)
root=buildtree(c)
codes=encode(root)
while True:
    try:
        s=input()
        if s[0] in {'0','1'}:
            print(decoding(root,s))
        else:
            print(encoding(codes,s))
            
    except EOFError:
         break
        
        
        
    