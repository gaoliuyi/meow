# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 19:20:52 2024

@author: ghp
"""
n=int(input())
ans=["-" for i in range(3**n)]
def cantor(start,end,level):
    if level==0:
        for i in range(start,end):
            ans[i]='*'
    else:
        cantor(start,start+(end-start)//3,level-1)
        cantor(start+(end-start)//3*2,end,level-1)
cantor(0,3**n,n)
print(''.join(ans))
        