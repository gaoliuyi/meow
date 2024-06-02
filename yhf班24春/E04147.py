# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:19:42 2024

@author: ghp
"""

n,a,b,c=input().split()
n=int(n)
p=[a,b,c]
def move(x,y,n):
    if n==1:
        print(f'{n}:{x}->{y}')
    else:
        for i in p :
            if i not in [x,y]:
                move(x,i,n-1)
                print(f'{n}:{x}->{y}')
                move(i,y,n-1)
move(a,c,n)