# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 20:02:50 2024

@author: ghp
"""

from itertools import product
def right_shift(row,shift):
    return row[-shift:]+row[:-shift]
def cal(mat):
    s=[0]*n
    for row in mat:
        for i in range(n):
            s[i]+=row[i]
    return max(s)
while True:
    n=int(input())
    if n==0:
        break
    mat=[]
    for i in range(n):
        mat.append(list(map(int,input().split())))
    sh=list(product(range(n),repeat=n))
    msum=float('inf')
    for h in sh:
        newmat=[right_shift(mat[i],h[i]) for i in range(n)]
        msum=min(msum,cal(newmat))
    print(msum)










