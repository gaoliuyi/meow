# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 16:27:50 2024

@author: ghp
"""

check=[1]*10002
check[1]=0
check[0]=0
for i in range(2,101):
    if check[i]==1:
        for j in range(2*i,10002,i):
            check[j]=0
n=int(input())
for i in range(2,n):
    if check[i]==1 and check[n-i]==1:
        print(i,n-i)
        break
            
