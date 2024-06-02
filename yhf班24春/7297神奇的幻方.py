# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 21:47:32 2024

@author: ghp
"""

n=int(input())
mat=[[0]*(2*n-1) for i in range(2*n-1)]
x=0
y=n-1
for i in range(1,(2*n-1)*(2*n-1)+1):
    mat[x][y]=i
    if x==0 and y==2*n-2:
        nx=x+1
    if x==0:
        nx=2*n-2
    else:
        nx=x-1
    if y==2*n-2:
        ny=0
    else:
        ny=y+1
    if mat[nx][ny]==0:
        x=nx
        y=ny
    else:
        x=x+1
        
for row in mat:
    print(*row)
    
    
